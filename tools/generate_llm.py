"""Regenerate the LLM page: python tools/generate_llm.py (standard library only)."""
from pathlib import Path
import re
from html import escape

root = Path(__file__).resolve().parents[1]
source = root / 'assets/llm/LLM_Topic_Index_Medium_Ranked_2026.md'
md = source.read_text(encoding='utf-8')
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
        content.append('</ul><div class="reading"><h4>Recommended reading <span>Medium</span></h4><ol>')
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
page = template.replace('<!-- TOPIC NAV -->', '\n'.join(nav)).replace('<!-- TOPICS -->', '\n'.join(content)).replace('<!-- NOTES -->', '\n'.join(notes))
(root/'_tabs/llm.html').write_text('---\ntitle: LLM\nlayout: false\nicon: fas fa-brain\norder: 2\npermalink: /llm/\n---\n'+page, encoding='utf-8')
print('Generated 60 topics, 204 subtopics, 1240 concepts and 612 reading links.')
