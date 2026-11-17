#!/usr/bin/env python3
"""Lint SQL migrations against wiki/concepts/standards/database.md.

  migration_lint.py FILE...           lint these files
  migration_lint.py --diff BASE HEAD  lint .sql files added or changed in BASE..HEAD

Fails on:
  client-grant      GRANT of table, view or sequence access to anon, authenticated
                    or PUBLIC (clients reach data only through the guard and RPCs;
                    GRANT EXECUTE on a function and USAGE on a schema are fine)
  default-privs     ALTER DEFAULT PRIVILEGES that grants to a client role
  rls-missing       CREATE TABLE in public without ENABLE ROW LEVEL SECURITY in the same file
  rls-disabled      ALTER TABLE ... DISABLE ROW LEVEL SECURITY
  definer-path      SECURITY DEFINER function without SET search_path
  prefix            object created in public without the repo's app prefix
                    (only when STANDARDS_DB_PREFIX is set, for example "lp_")

Suppress one statement with a `-- lint:allow <rule> <reason>` comment inside it or
after its semicolon on the same line. Every suppression needs a reason.
The shared database enforces client-grant and rls-missing itself (event trigger
platform_client_lockdown); this lint catches them before merge.
"""
import os, re, subprocess, sys

CLIENT = r'(?:anon|authenticated|public)'
MIGRATION_DIRS = ('migrations/', 'supabase/migrations/', 'sql/', 'db/')


def strip_comments(sql):
    allows = set(re.findall(r'--\s*lint:allow\s+([a-z-]+)', sql, re.I))
    sql = re.sub(r'/\*.*?\*/', ' ', sql, flags=re.S)
    sql = re.sub(r'--[^\n]*', ' ', sql)
    return sql, allows


def statements(sql):
    """Split on semicolons outside dollar-quoted bodies and string literals."""
    out, buf, i, n = [], [], 0, len(sql)
    dollar = None
    in_str = False
    while i < n:
        c = sql[i]
        if dollar:
            if sql.startswith(dollar, i):
                buf.append(dollar); i += len(dollar); dollar = None; continue
        elif in_str:
            if c == "'":
                in_str = False
        elif c == "'":
            in_str = True
        elif c == '$':
            m = re.match(r'\$[A-Za-z_0-9]*\$', sql[i:])
            if m:
                dollar = m.group(0); buf.append(dollar); i += len(dollar); continue
        elif c == ';':
            out.append(''.join(buf)); buf = []; i += 1; continue
        buf.append(c); i += 1
    if ''.join(buf).strip():
        out.append(''.join(buf))
    return out


def raw_statements(text):
    """Statements with comments kept, to read lint:allow markers per statement."""
    return statements(text)


def lint_text(name, text, prefix=None):
    errs = []
    raw = raw_statements(text)
    body_all, _ = strip_comments(text)
    rls_enabled = {m.lower().split('.')[-1].strip('"') for m in re.findall(
        r'alter\s+table\s+(?:if\s+exists\s+)?(?:only\s+)?([\w."]+)\s+enable\s+row\s+level\s+security', body_all, re.I)}
    pos = 0
    for idx, st_raw in enumerate(raw):
        start = text.find(st_raw, pos)
        start = pos if start < 0 else start
        pos = start + len(st_raw)
        # line of the first non-comment, non-blank line of the statement
        lead = re.match(r'(?:\s|--[^\n]*\n|/\*.*?\*/)*', st_raw, re.S).end()
        line = text[:start + lead].count('\n') + 1
        st, allows = strip_comments(st_raw)
        # a `-- lint:allow` after the semicolon on the same line belongs to this statement
        if idx + 1 < len(raw):
            allows |= set(re.findall(r'--\s*lint:allow\s+([a-z-]+)', raw[idx + 1].split('\n', 1)[0], re.I))
        s = ' '.join(st.split())
        if not s:
            continue
        low = s.lower()

        def err(rule, msg):
            if rule not in allows:
                errs.append(f'{name}:{line}: {rule}: {msg}')

        if low.startswith('grant ') and re.search(rf'\bto\s+(?:[\w",\s]*\b)?{CLIENT}\b', low):
            if not re.search(r'\bon\s+(?:all\s+)?(?:functions?|routines?|procedures?|schema)\b', low) \
                    and not re.match(r'grant\s+(?:execute|usage)\b(?!.*\bon\s+(?:table|all\s+tables|sequence|all\s+sequences))', low):
                err('client-grant', 'client roles may not be granted table, view or sequence access; use the guard and an RPC')
        if low.startswith('alter default privileges') and re.search(rf'\bgrant\b.*\bto\s+(?:[\w",\s]*\b)?{CLIENT}\b', low) \
                and not re.search(r'\bon\s+(?:functions|routines|schemas)\b', low):
            err('default-privs', 'default privileges may not grant client roles access')
        m = re.match(r'create\s+(?:unlogged\s+)?table\s+(?:if\s+not\s+exists\s+)?([\w."]+)', low)
        if m:
            ident = m.group(1).replace('"', '')
            schema, _, tbl = ident.rpartition('.')
            if schema in ('', 'public'):
                if tbl not in rls_enabled:
                    err('rls-missing', f'table {ident} needs ALTER TABLE ... ENABLE ROW LEVEL SECURITY in the same migration')
                if prefix and not tbl.startswith(prefix):
                    err('prefix', f'table {ident} must start with {prefix}')
        if re.search(r'\bdisable\s+row\s+level\s+security\b', low):
            err('rls-disabled', 'never disable RLS')
        if re.match(r'create\s+(?:or\s+replace\s+)?(?:function|procedure)\b', low):
            if 'security definer' in low and not re.search(r'\bset\s+search_path\b', low):
                err('definer-path', 'SECURITY DEFINER needs SET search_path (use \'\' or pg_catalog, public)')
            fm = re.match(r'create\s+(?:or\s+replace\s+)?(?:function|procedure)\s+([\w."]+)', low)
            if prefix and fm:
                ident = fm.group(1).replace('"', '')
                schema, _, fn = ident.rpartition('.')
                if schema in ('', 'public') and not fn.startswith(prefix):
                    err('prefix', f'function {ident} must start with {prefix}')
    return errs


def changed_sql(base, head):
    out = subprocess.run(['git', 'diff', '--name-only', '--diff-filter=AM', f'{base}...{head}'],
                         capture_output=True, text=True, check=True).stdout.split()
    return [f for f in out if f.endswith('.sql') and (any(d in f for d in MIGRATION_DIRS)) and os.path.exists(f)]


def main(argv):
    if argv[:1] == ['--diff']:
        files = changed_sql(argv[1], argv[2])
    else:
        files = argv
    prefix = os.environ.get('STANDARDS_DB_PREFIX') or None
    errs = []
    for f in files:
        errs += lint_text(f, open(f, encoding='utf-8', errors='replace').read(), prefix)
    for e in errs:
        print(e)
    print(f'migration-lint: {len(files)} file(s), {len(errs)} problem(s)')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
