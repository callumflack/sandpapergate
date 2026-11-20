# Public Sandpapergate site

- Public reference edition under Callum Flack’s ownership. Main is protected for contributors. Callum retains owner/admin bypass and may push directly; owner-authorised delivery requests may use that access. External and non-admin contributions require a PR, Callum’s CODEOWNER approval and passing checks. Do not approve on his behalf. No publication beyond the existing Cloudflare Worker without matching user authority.
- Read README.md and CONTRIBUTING.md. MDX in src/content/docs is the public authoring source; sources.json and claims.json under public are agent-readable metadata. Keep those consistent. Never import or publish the private source corpus or local research logs.
- Preserve source IDs, dates and paragraph locators. Distinguish allegations, denials, qualified recollections, publisher framing and archive reasoning. Do not close a listening/source gap without actual evidence.
- Headings, description and body share their parent width; no character-width hacks or manual body line breaks.
- Checks: npm run format:check, npm run build, npm run check, npm run verify:public; observe changed production-preview pages/search.

## Deployment

All production deployments and rollbacks must go through [the public repository’s GitHub Actions workflow](https://github.com/callumflack/sandpapergate/blob/main/.github/workflows/check.yml). Authorized changes reach `main` through an approved contributor PR or an owner-authorized direct push. CI runs the checks, builds the site and deploys that exact verified artifact to the existing Cloudflare Worker.

Do not upload folders in the Cloudflare dashboard, run a local `wrangler deploy`, call deployment APIs directly, or use a manual fallback. If CI fails, fix the workflow or report the blocker. Roll back by reverting or correcting `main` and letting CI deploy it.

A push alone is not a completed deployment. Confirm the checks and deployment jobs passed for the intended commit, then verify the relevant live pages. The private research build must remain local.

## Source titles

Name the event or document in the title. Use the status label for transcript method, verification and completeness. Use a publisher or date to distinguish editions where needed. Preserve source IDs, URLs and exact citations when editing titles.

## Questions index

Use chronology for the groups and importance within each group. Lead with the question whose answer would most change a reader’s understanding of that part of the dispute. For the tour, who knew and when comes before whether use began at Port Elizabeth.

Follow with the accounts and evidence needed to test the lead question, then narrower roles or consequences. Put institutional procedure after player accounts where it supplies context. Rank open and linked questions by the same standard. After editing [the Questions index](./src/content/docs/questions/index.mdx), read back the order in every group on the rendered Questions page.
