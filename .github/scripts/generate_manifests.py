"""Write MANIFEST.json for every playbook directory (one with NN-*.md chapters)."""
import glob
import json
import os
import re

for d in sorted(p.rstrip('/') for p in glob.glob('*/')):
    if d.startswith('.') or not glob.glob(f'{d}/[0-9][0-9]-*.md'):
        continue
    print(f'Generating MANIFEST.json for {d}')
    path = f'{d}/MANIFEST.json'

    # Preserve existing metadata if MANIFEST.json exists
    old = {}
    if os.path.exists(path):
        try:
            with open(path) as fh:
                old = json.load(fh)
        except ValueError:
            old = {}

    chapters = []
    # Add README.md as Overview if it exists
    if os.path.exists(f'{d}/README.md'):
        chapters.append({'file': 'README.md', 'title': 'Overview', 'num': '00'})
    # Add numbered chapters, titled by their first H1
    for f in sorted(glob.glob(f'{d}/[0-9][0-9]-*.md')):
        fname = os.path.basename(f)
        title = ''
        with open(f) as fh:
            for line in fh:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
        if not title:
            title = re.sub(r'^[0-9]+-', '', fname.replace('.md', '').replace('-', ' '))
        chapters.append({'file': fname, 'title': title, 'num': fname[:2]})
    # Keep appendix pages (unnumbered files listed in the old manifest) after the chapters
    listed = {c['file'] for c in chapters}
    for c in old.get('chapters', []):
        if c.get('file') not in listed and os.path.exists(f"{d}/{c.get('file')}"):
            c = dict(c, num=f'{len(chapters):02d}')
            chapters.append(c)
            listed.add(c['file'])

    manifest = {'id': old.get('id') or d, 'title': old.get('title') or d.replace('-', ' ').upper()}
    if old.get('icon'):
        manifest['icon'] = old['icon']
    if old.get('description'):
        manifest['description'] = old['description']
    manifest['chapters'] = chapters

    with open(path, 'w') as out:
        json.dump(manifest, out, indent=2)
        out.write('\n')
