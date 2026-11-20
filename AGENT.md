# Public Sandpapergate site

- Public reference edition under Callum Flack’s ownership. Main is protected; all changes go through a PR and require his approval. Do not bypass protection or approve on his behalf. No publication beyond the existing Cloudflare Worker without matching user authority.
- Read README.md and CONTRIBUTING.md. MDX in src/content/docs is the public authoring source; sources.json and claims.json under public are agent-readable metadata. Keep those consistent. Never import or publish the private source corpus or local research logs.
- Preserve source IDs, dates and paragraph locators. Distinguish allegations, denials, qualified recollections, publisher framing and archive reasoning. Do not close a listening/source gap without actual evidence.
- Headings, description and body share their parent width; no character-width hacks or manual body line breaks.
- Checks: npm run format:check, npm run build, npm run check, npm run verify:public; observe changed production-preview pages/search.
