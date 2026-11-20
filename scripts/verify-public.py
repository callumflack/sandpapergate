"""Verify the public reference edition and its actual built citation links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=set();self.links=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
pages={p.relative_to(DIST).as_posix():Page(p.read_text()) for p in DIST.rglob('*.html')}
assert pages,'Build the site first'
assert not (ROOT/'research').exists(),'Private research must not enter the public checkout'
for name in ['research','artifacts','.git','.env']:
 assert not (DIST/name).exists(),f'Private path published: {name}'
for directory in ['src','public']:
 for p in (ROOT/directory).rglob('*'):
  if p.is_file() and p.suffix in ['.mdx','.json','.ts','.astro']:
   text=p.read_text()
   assert '/Users/' not in text and '/private/tmp/' not in text,f'Private filesystem path: {p}'
   if p.suffix=='.json':assert '"text_blocks"' not in text,f'Captured source body: {p}'
links=0
for filename,page in pages.items():
 for href in page.links:
  u=urlsplit(href)
  if u.scheme or u.netloc or (u.path and not u.path.startswith('/')):continue
  dest=unquote(u.path).lstrip('/') if u.path else filename
  if u.path.endswith('/'):dest+='index.html'
  if not dest:dest='index.html'
  assert (DIST/dest).is_file(),f'{filename}: missing {href}'
  if u.fragment and dest.endswith('.html'):assert unquote(u.fragment) in pages[dest].ids,f'{filename}: missing anchor {href}'
  links+=1
manifest=json.loads((DIST/'sources.json').read_text())
assert manifest['publication_status']=='public-reference-edition'
byid={s['id']:s for s in manifest['sources']}
locators=0
for s in byid.values():
 assert s['source_text_published'] is False
 page=pages[s['url'].lstrip('/')+'index.html']
 for url in s['paragraph_urls']:
  assert urlsplit(url).fragment in page.ids,(s['id'],url)
  locators+=1
claim_manifest=json.loads((DIST/'claims.json').read_text())
claims=claim_manifest['claims']+claim_manifest['khawaja_claims'];refs=0
for claim in claims:
 groups=[claim['supporting'],claim['challenging']]
 if 'basis' in claim:groups.append([{'refs':claim['basis']['refs']}])
 for arguments in groups:
  for argument in arguments:
   for ref in argument['refs']:
    sid=manifest['aliases'].get(ref['source'],ref['source']);s=byid[sid]
    page=pages[s['url'].lstrip('/')+'index.html']
    argument_page=pages['questions/'+claim['slug']+'/index.html']
    for block in ref['blocks']:
     assert block in page.ids
     assert s['url']+'#'+block in argument_page.links
     refs+=1
assert (DIST/'pagefind/pagefind.js').is_file()
assert (DIST/'llms.txt').is_file() and (DIST/'llms-full.txt').is_file()
assert len(re.findall(r'href="/people/[^/#]+/"',(DIST/'people/index.html').read_text()))==17
print(f'Public edition verified: {len(pages)} HTML pages, {links} local links, {locators} citation locators, {refs} claim references; private captures excluded.')
