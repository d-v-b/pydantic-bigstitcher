# Releasing

Releases are automated via GitHub Actions (`.github/workflows/release.yml`).
The version comes from the git tag (`hatch-vcs`); there is no version file to edit.

## One-time setup (already done if a release has succeeded before)

1. **PyPI Trusted Publisher** — at <https://pypi.org/manage/account/publishing/>, add a
   GitHub publisher: owner `d-v-b`, repo `pydantic-bigstitcher`, workflow `release.yml`,
   environment `pypi`.
2. **TestPyPI Trusted Publisher** — same at <https://test.pypi.org/manage/account/publishing/>,
   environment `testpypi`.
3. **GitHub Environments** — create `pypi` and `testpypi` (repo Settings → Environments).
   Add a **required reviewer** on `pypi` so every real publish needs a human approval.
4. **GitHub Pages** — enable Pages (Settings → Pages) with source = `gh-pages` branch so
   the docs site serves. The first docs deploy creates the `gh-pages` branch.

## Cutting a release

```bash
gh release create vX.Y.Z --generate-notes --title "vX.Y.Z"
```

This creates the tag and the GitHub Release, which fires the workflow:
`test → build → TestPyPI (non-blocking) → PyPI → attach artifacts → deploy docs`.

Approve the `pypi` environment when prompted. No tokens, no manual build, no version bump.
PEP 740 attestations are produced automatically.
