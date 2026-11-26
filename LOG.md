# Public release worklog

## 26 November 2026 — Khawaja’s captaincy allegation

Callum asked for the book’s allegation and its stated basis to be published. The existing question now leads with the memoir passage quoted by AAP. The ABC interview and Cummins’s reply are dated separately. The extract does not establish the selectors’ actual motive.

## 26 November 2026 — Cummins press conference transcript

Callum requested the full press conference under Documents. SP070 is the archive’s own automatic transcript of the SEN podcast. The public reading copy keeps the recording timestamps and paragraph IDs, omits the advertisements and links the captaincy exchange. The wording and speaker turns still require checking against the recording. The existing GitHub Actions workflow owns publication.

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

## 20 November 2026 — Full accumulated archive update

Callum authorised committing and deploying all dirty work, including other agents’ changes. Prepared all current question/claim/coverage/editorial/typography changes for this public reference edition; protected main, sole CODEOWNER and manual Cloudflare release remain intact. The private corpus and logs remain separate. Source IDs/locators preserved, fourteen Khawaja claims exported, public verifier covers both claim sets and allegation-basis links. Pending required checks, PR, Callum review/merge and production deployment.

### Header badge removal

Callum asked to remove the “Public record” label beside Search. Removed that badge and its styles from this release checkout. An isolated build and the public archive verifier passed after the change.

## 20 November 2026 — Restore owner access, protect contributor merges

Callum explicitly corrected the policy: PR/CODEOWNER controls are for external contributors; he must retain direct-push access. Verified he is the only repository collaborator/admin and no additional rulesets exist. Permanent requested configuration: disable only admin enforcement on the existing main protection; retain one Callum CODEOWNER review, stale dismissal, strict Public site checks, conversation/linear-history rules and no force pushes/deletions for contributors. This is the requested owner access policy, not a temporary operational override. Delivery proceeds by an owner-authorised direct push and existing manual Cloudflare release. Documentation reconciled with this authority.

## 20 November 2026 — Verified source-title handoff

Callum authorised the content chat to hand over25 verified title changes for commit/deploy; both roots are stable and that chat is holding writes. Reviewed58 titles. Pat Cummins’s13November press conference now has a human-readable event title while the transcript badge retains verification status. Source IDs, URLs, locators and frozen source text/hashes preserved. Peer reports full format/build/Astro/Nimbus and archive/public proof; root independently confirms captured long paragraphs remain excluded from public MDX. The Port Elizabeth comparison and short answer remain private under Callum’s explicit hold.

The complete release has been committed and manually verified through93fe1a6. Root is committing this final title handoff; analytics/CI chat owns PR2 and the explicitly approved Worker-only Editor token in GitHub production(main only). No new1Password access or broader credentials authorised. Automatic main deployment remains to be observed after that workflow merge.

## 20 November 2026 — Require CI for every deployment

Callum explicitly required all deployments to go through CI, with no more manual uploads. Root owns this policy update in both checkouts. AGENTS.md routes every agent to the Deployment section in AGENT.md; README explains the same delivery path. Removed the stale private instruction that deployments were manual. Dashboard uploads, local Wrangler deploys, direct deployment API calls and manual fallbacks are prohibited. Failed CI must be repaired or reported; rollback goes through a revert/correction on main and the same workflow. A deployment is complete only after the matching commit’s checks and deployment jobs pass and the live result is verified. Owner direct-push access and private corpus boundaries remain unchanged.

Notified the active content and announcement chats directly. The former analytics/CI chat is archived and cannot receive messages; its future sessions will load the committed repository instructions. Public instructions will be delivered through the existing CI workflow; no manual deployment is authorized.

## 20 November 2026 — Publish supplied SP024 interview transcript

Callum explicitly requested the full ABC 7.30 interview transcript on the existing SP024 public document page and supplied its local raw capture. This is a source-specific publication instruction. Root owns the page, consistent manifest/notices, required checks, owner-authorised direct push and CI-only deployment; no other captured source text is authorised for publication.

Replaced the 63 empty locators with the 63 supplied transcript paragraphs, preserving p-001 through p-063 and the original publisher attribution/date. Updated SP024 publication status and its stale acquisition task; independent comparison with the recording remains open. The public verifier retains its private-text restriction for every other source. Local formatting, build, Astro diagnostics, documentation lint and public archive verification pass (123 HTML pages, 3483 locators, 895 claim references). Parsed built HTML matches all 63 supplied transcript paragraphs exactly, in order. Required media audit and existing 10 MiB pre-commit hook cover the commit. CI deployment and live verification pending.
