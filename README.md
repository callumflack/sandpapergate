# Sandpapergate

[Read the archive](https://sandpapergate.callumflack-97f.workers.dev/) · [Agent index](https://sandpapergate.callumflack-97f.workers.dev/llms.txt)

A public source catalogue and argument map for the 2018 South Africa tour and subsequent accounts. Claims, responses and unresolved questions are distinguished; there is no prescribed verdict.

The public edition contains original archive analysis, source metadata and citation locators. Full downloaded publisher articles, memoir excerpts, PDFs, recordings and automatic transcripts are not included. Follow original publisher links to read underlying sources. Collection/completeness labels describe the private research capture, not a full-text copy on this site. Missing source and listening checks remain visible.

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

GitHub Actions checks every PR. PR checks have read-only repository access and do not deploy or receive publication credentials. The initial Cloudflare release is a direct upload of the checked build. Changes to `main` do not automatically deploy yet. Build and verify the protected main revision, then upload `dist` through Cloudflare or use its Wrangler configuration with your own authorised Cloudflare session.
