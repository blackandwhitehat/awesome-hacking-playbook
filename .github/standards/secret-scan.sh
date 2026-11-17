#!/usr/bin/env bash
# Secret scan used by the pre-commit hook, CI and repo_audit.
#   secret-scan.sh staged            scan what is staged for commit
#   secret-scan.sh range BASE HEAD   scan commits in BASE..HEAD (CI on a PR)
#   secret-scan.sh tree DIR          scan a working tree (audit)
# Fails (exit 1) on any custom-detector hit (our Supabase, guard, RevenueCat,
# Cloudflare formats) or any built-in detector verified live.
# Prints detector, file and line only. Never prints a secret value.
# Bypass for a known false positive: put `trufflehog:ignore` on that line.
set -u
TH="${TRUFFLEHOG:-$(command -v trufflehog || echo "$HOME/bin/trufflehog")}"
CFG="${TRUFFLEHOG_CONFIG:-$(dirname "$0")/trufflehog.yaml}"
mode="${1:-staged}"
EXC="${TRUFFLEHOG_EXCLUDE:-$(dirname "$0")/exclude-paths.txt}"
common=(--config "$CFG" --json --no-update --results=verified,unknown,unverified)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
case "$mode" in
  staged)
    root=$(git rev-parse --show-toplevel) || exit 0
    git diff --cached --name-only --diff-filter=ACMR -z | while IFS= read -r -d '' f; do
      mkdir -p "$tmp/$(dirname "$f")"; git show ":$f" > "$tmp/$f" 2>/dev/null
    done
    [ -z "$(ls -A "$tmp")" ] && exit 0
    "$TH" filesystem "$tmp" "${common[@]}" > "$tmp.out" 2>/dev/null ;;
  range)
    "$TH" git "file://$(git rev-parse --show-toplevel)" --since-commit "$2" --branch "${3:-HEAD}" "${common[@]}" > "$tmp.out" 2>/dev/null ;;
  tree)
    "$TH" filesystem "${2:-.}" --exclude-paths "$EXC" "${common[@]}" > "$tmp.out" 2>/dev/null ;;
  *) echo "usage: $0 staged|range BASE HEAD|tree DIR" >&2; exit 2 ;;
esac
hits=$(python3 -I - "$tmp.out" "$tmp" <<'PY'
import json, sys
out, prefix = sys.argv[1], sys.argv[2] + '/'
for line in open(out):
    try: r = json.loads(line)
    except Exception: continue
    custom = r.get('DetectorName') == 'CustomRegex'
    if not (custom or r.get('Verified')): continue
    name = (r.get('ExtraData') or {}).get('name') if custom else r.get('DetectorName') + ' (verified live)'
    d = r.get('SourceMetadata', {}).get('Data', {})
    src = d.get('Git') or d.get('Filesystem') or {}
    f = (src.get('file') or '').replace(prefix, '')
    print(f"  {name}: {f}:{src.get('line', '?')}" + (f" (commit {src['commit'][:8]})" if src.get('commit') else ''))
PY
)
rm -f "$tmp.out"
if [ -n "$hits" ]; then
  echo "secret-scan: secrets found. Remove them, move the value to a secret store, and rotate it if it was ever pushed." >&2
  echo "$hits" | sort -u >&2
  exit 1
fi
exit 0
