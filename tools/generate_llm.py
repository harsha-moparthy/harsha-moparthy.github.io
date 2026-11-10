"""Regenerate the LLM page: python tools/generate_llm.py (standard library only)."""
from pathlib import Path
import re
import json
from html import escape

root = Path(__file__).resolve().parents[1]
source = root / 'assets/llm/LLM_Topic_Index_Medium_Ranked_2026.md'
md = source.read_text(encoding='utf-8')
catalog, curated = {}, {}
batches = sorted((root/'tools/curation-batches').glob('*.json'))
for batch_path in batches:
    batch = json.loads(batch_path.read_text(encoding='utf-8'))
    assert not (catalog.keys() & batch['sources'].keys()), 'Duplicate source IDs'
    assert not (curated.keys() & batch['subtopics'].keys()), 'Duplicate subtopic batches'
    catalog.update(batch['sources'])
    curated.update(batch['subtopics'])
for num, ids in curated.items():
    assert len(ids) >= 3 and len(ids) == len(set(ids)), num
    assert all(i in catalog for i in ids), num
    assert all(catalog[i][2].startswith('https://') for i in ids), num
def inline(text):
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\((https://[^\s)]+)\)', r'<a href="\2">\1</a>', text)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
def slug(text):
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')
resources = {}
for line in md.splitlines():
    if line.startswith('| ['):
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) == 6:
            key = re.search(r'\]\(#([^)]*)\)', cells[1]).group(1)
            resources[key] = cells[3:]
topics = []
for line in md.splitlines():
    match = re.match(r'## (\d{2})\. (.+)', line)
    sub = re.match(r'### (\d{2}\.\d+) (.+)', line)
    if match:
        topics.append({'num': match[1], 'title': match[2], 'id': slug(match[1]+' '+match[2]), 'subs': []})
    elif sub:
        topics[-1]['subs'].append({'title': sub[2], 'num': sub[1], 'id': slug(sub[1]+' '+sub[2]), 'items': []})
    elif line.startswith('- [ ] '):
        topics[-1]['subs'][-1]['items'].append(line[6:])
assert len(topics) == 60
assert sum(len(t['subs']) for t in topics) == len(resources) == 204
assert sum(len(s['items']) for t in topics for s in t['subs']) == 1240
nav, content = [], []
for t in topics:
    count = sum(len(s['items']) for s in t['subs'])
    nav.append(f'<a href="#{t["id"]}"><span>{t["num"]}</span>{escape(t["title"])}</a>')
    content.append(f'<details class="topic" id="{t["id"]}"><summary><span class="number">{t["num"]}</span><span class="topic-title">{escape(t["title"])}<small>{len(t["subs"])} subtopics Â· {count} concepts</small></span><span class="chevron" aria-hidden="true">+</span></summary><div class="topic-body">')
    for s in t['subs']:
        content.append(f'<section class="subtopic" id="{s["id"]}"><h3><a href="#{s["id"]}">{s["num"]}</a> {escape(s["title"])}</h3><ul class="checklist">')
        for i, item in enumerate(s['items']):
            content.append(f'<li><label><input type="checkbox" data-key="{s["num"]}-{i}"><span>{escape(item)}</span></label></li>')
        content.append('</ul><div class="reading"><h4>Recommended reading <span>'+('Curated path' if s['num'] in curated else 'Original candidates')+'</span></h4><ol>')
        if s['num'] in curated:
            for rid in curated[s['num']]:
                publisher, title, url, kind, why = catalog[rid]
                content.append(f'<li class="curated-resource"><a href="{escape(url, quote=True)}">{escape(title)}</a><small>{escape(publisher)} · {escape(kind)}</small><p>{escape(why)}</p></li>')
        else:
            for resource in resources[s['id']]:
                content.append('<li>'+inline(re.sub(r'\[#\d: ', '[', resource))+'</li>')
        content.append('</ol></div></section>')
    content.append('</div></details>')
notes = []
for line in md[md.index('## D. '):].splitlines():
    if line.startswith('## '): notes.append('<h3>'+escape(line[3:])+'</h3>')
    elif line.startswith('- '): notes.append('<p>'+inline(line[2:])+'</p>')
    elif line.strip(): notes.append('<p>'+inline(line)+'</p>')
template = (root/'tools/llm-template.html').read_text(encoding='utf-8')
page = template.replace('<!-- TOPIC NAV -->', '\n'.join(nav)).replace('<!-- TOPICS -->', '\n'.join(content)).replace('<!-- NOTES -->', '\n'.join(notes)).replace('<!-- CURATION COUNT -->', str(len(curated)))
(root/'_tabs/llm.html').write_text('---\ntitle: LLM\nlayout: false\nicon: fas fa-brain\norder: 2\npermalink: /llm/\n---\n'+page, encoding='utf-8')
valid_nums = {s['num'] for t in topics for s in t['subs']}
assert curated.keys() <= valid_nums
guide = ['# LLM Atlas: Curated Reading Guide', '', f'Updated 10 November 2026. {len(curated)} of 204 subtopics curated.', '', 'Read each list in order: orientation, explanation, implementation, or deeper theory. These are editorial learning paths, not popularity rankings. Sources were inspected through publisher pages or search excerpts; this is not a claim that every technical statement was independently reproduced. Older articles remain where they explain durable foundations. No claim of exhaustive concept coverage is made. Original Medium candidates are retained in the source index, not endorsed by this guide.', '']
for t in topics:
    guide += [f'## {t["num"]}. {t["title"]}', '']
    for s in t['subs']:
        guide += [f'### {s["num"]} {s["title"]}', '']
        guide += ['- [ ] '+item for item in s['items']] + ['']
        if s['num'] in curated:
            for n, rid in enumerate(curated[s['num']], 1):
                publisher, title, url, kind, why = catalog[rid]
                guide += [f'{n}. [{title}]({url}) — {publisher} · {kind}. {why}']
        else: guide += ['Reading-list review pending; see the original index for candidate links.']
        guide += ['']
(root/'assets/llm/LLM_Topic_Index_Curated_2026.md').write_text('\n'.join(guide), encoding='utf-8')
pending = [s['num'] for t in topics for s in t['subs'] if s['num'] not in curated]
(root/'tools/LLM_CURATION_PROGRESS.md').write_text(f'# Reading-list curation checkpoint\n\nCompleted: {len(curated)}/204 subtopics across {len(batches)} published-batch files.\nUnique sources: {len(catalog)}.\n\nNext subtopics: '+', '.join(pending[:10])+'\n\nRemaining: '+', '.join(pending)+'\n\nResume by inspecting the next ten subtopics and adding the next numbered JSON file in tools/curation-batches/. Regenerate with python tools/generate_llm.py, verify, commit, and push each batch. Do not mark a source checked solely because its URL responds.\n', encoding='utf-8')
print(f'Generated 60 topics, 204 subtopics, 1240 concepts; {len(curated)} curated reading paths, {len(catalog)} unique sources.')
