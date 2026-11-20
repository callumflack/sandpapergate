# Sandpapergate

[Read the archive](https://sandpapergate.callumflack-97f.workers.dev/) · [Agent index](https://sandpapergate.callumflack-97f.workers.dev/llms.txt)

A public source catalogue and argument map for the 2018 South Africa tour and subsequent accounts. Claims, responses and unresolved questions are distinguished; there is no prescribed verdict.

The public edition contains original archive analysis, source metadata and citation locators. SP024 includes the full ABC 7.30 interview transcript supplied for publication. Other downloaded publisher articles, memoir excerpts, PDFs, recordings and automatic transcripts remain private. Follow original publisher links for those sources. Collection/completeness labels describe the research capture; missing source and listening checks remain visible.

## Local development

Requires Node24 and npm.

```sh
npm ci
npm run build
npm run check
npm run verify:public
npm run preview -- --host 127.0.0.1 --port 4329
```

Open http://localhost:4329/. Search uses the built Pagefind index.

## Contributions

Fork the repository and open a pull request to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md). Callum Flack is the sole code owner. Main requires his approving review, a passing public-site check, resolved conversations and current reviews; force pushes and branch deletion are disabled. Callum retains owner/admin bypass so he can push his own changes directly. Review and check requirements remain in place for external and non-admin contributors.

The Questions index groups the dispute chronologically and ranks questions by importance within each group. A fourteen-claim Khawaja dossier, a detailed witness/denial comparison and separate Cummins questions link to source locators and preserve open issues. The claim manifest exports both the broader maps and the Khawaja dossier.

The public MDX pages in `src/content/docs` are editable source, not regenerated from private files. `public/sources.json` and `public/claims.json` are the agent-readable catalogues; keep their metadata and claims consistent with related reading pages. Source paragraph IDs are stable citation locators.

## Hosting

GitHub Actions checks every PR and push to `main`. After the checks pass on `main`, the deployment job publishes that same verified build to the existing `sandpapergate` Cloudflare Worker. Deployments run one at a time, and an older build is skipped if `main` has moved. The `production` environment supplies the Worker-scoped credential to the deployment job.

All deployments and rollbacks go through [this workflow](.github/workflows/check.yml). Do not upload folders through the Cloudflare dashboard, deploy with local Wrangler or direct API calls, or fall back to manual deployment when CI fails. Fix CI or report the blocker. To roll back, revert or correct `main` and let CI deploy it. After deployment, confirm the matching commit’s checks and deployment jobs succeeded and verify the live site. See [the agent deployment instructions](AGENT.md#deployment).
