# Public release worklog

## 20 November 2026 — Initial public reference edition

Authorised by Callum: publish the site and public repository under callumflack; accept PRs while requiring his merge authorisation. Full third-party source text and all private research files remain excluded. Source catalogue, original archive analysis, stable citation locators and open source/listening gaps are included. Main will require CODEOWNER approval, public-site checks and resolved conversations, with admin enforcement and no force pushes/deletion.

Root owns preparation, checks, GitHub configuration and live verification. No other repository writers. Initial bootstrap is the first remote content, followed by new branch protection; no pre-existing rule is disabled.

Open: local validation, initial public push, read-back of repository protection, successful Cloudflare build and live route/search verification.

## 20 November — Hosting correction and visual feedback

User selected Cloudflare, superseding the planned GitHubPages host. Latest Scrawl applied: looser desktopheadline tracking with1pxreduction, redundant statsrule removed, CA/ICC combined under Governing bodies. Public origin will be set from actual Cloudflare project, not an assumed domain. Connector lacks deployment scopes; dashboard access being checked.

- Authenticated personal Cloudflare dashboard available in Chrome; no credential access needed. Existing account subdomain verified as callumflack-97f.workers.dev. Worker target sandpapergate, expected production origin https://sandpapergate.callumflack-97f.workers.dev. Restored the original Nimbus scaffold’s Wrangler static-assets configuration for this Cloudflare release; same hosting pattern as the existing Agents Field Guide. Native connector deployment scopes unavailable; use authenticated dashboard Git integration.

- Public build/local authoring/link checks pass;105pages,6260local links,3483citationlocators,320claimreferences. Privacy comparison confirms1222sourceparagraphs longer than25words absent from public MDX; no private research directory exported.
- Scrawl rendered proof confirms61pxheadline/−.035emtracking, desktopsecondline retained, stats lowerborder0px. Governing bodies merged.
- Cloudflare Git connection requested a new account-level GitHub app authorisation. Cancelled that request; no new GitHub access granted. Use direct upload of the checked public build for initial release instead. Main/PR checks remain GitHub-owned; automatic deployment on merge is not configured.

- Initial commit stopped before any remote repository was created: imported KB size-hook installer assumed KB-only helper/layout scripts absent here. Replaced that inapplicable local hook with a repository-owned staged-blob10MiBguard. No guard bypass. Removed two trailing-whitespace lines in copied Nimbus components; no behaviour change. Public code is still unpushed pending initial commit and protection setup.
