# Release Workflow Design — GHA + PyPI Trusted Publishing

**Date:** 2026-05-29
**Branch:** `add-release-workflow` (worktree at `../pbs-release`)

## Problem

Releases are fully manual: bump `__about__.py`, commit "version bump", tag `vX.Y.Z`,
`hatch build`, `hatch publish` with a token, optionally `mkdocs gh-deploy`. There is no
CI for releases (only `test.yml`). This is error-prone (version drift, stale `dist/`,
token handling) and undocumented.

Goal: a modern GitHub Actions workflow that builds and publishes to PyPI via OIDC
Trusted Publishing (no long-lived tokens), gated on tests, triggered by publishing a
GitHub Release.

## Decisions

- **Trigger:** `on: release: { types: [published] }`. Releasing is `gh release create vX.Y.Z`.
- **Version source:** switch to `hatch-vcs` — version derived from the git tag. No version literal in the repo.
- **Publish targets:** TestPyPI first (non-blocking), then PyPI. Both via Trusted Publishing (OIDC), no tokens.
- **Test gate:** refactor `test.yml` to be reusable (`workflow_call`); release workflow `uses:` it.
- **Version guard:** build job asserts the built artifact version equals the tag (fails on `.devN+g<sha>`, i.e. untagged/dirty build).
- **Runtime version:** `importlib.metadata.version("pydantic-bigstitcher")` exposed as `__init__.__version__`.
- **PEP 740 attestations:** kept ON (the `pypa/gh-action-pypi-publish` default `attestations: true`). Free signed provenance uploaded to PyPI via the existing `id-token: write`; no extra job or permission. We skip only the separate `sigstore/gh-action-sigstore-python` job (redundant).
- **Action pinning:** third-party actions pinned to major-version tags (`@release/v1`, `@v4`); Dependabot already bumps them.
- **Docs:** `mkdocs gh-deploy` runs on release after PyPI publish.

## Build-system change: hatch → hatch-vcs

- `pyproject.toml` `[build-system]`: `requires = ["hatchling", "hatch-vcs"]`.
- Replace path-based `[tool.hatch.version]` with:
  ```toml
  [tool.hatch.version]
  source = "vcs"
  ```
- **Delete** `src/pydantic_bigstitcher/__about__.py`.
- Remove the `__about__.py` entry from `[tool.coverage.run] omit`.
- In `src/pydantic_bigstitcher/__init__.py`:

  ```python
  from importlib.metadata import version

  __version__ = version("pydantic-bigstitcher")
  ```

- Tag `v0.0.11` → built version `0.0.11` (hatch-vcs strips the leading `v`).

## test.yml refactor (reusable)

Add `workflow_call:` to the existing `on:` triggers (keep `push`/`pull_request`/`workflow_dispatch`).
No change to the matrix or steps. Normal CI behavior is unchanged; the release workflow can now call it.

## release.yml — job graph

Trigger: `on: release: { types: [published] }`. Per-job least-privilege `permissions`.

1. **test** — `uses: ./.github/workflows/test.yml`. Gate: nothing publishes unless the 3.10–3.12 matrix is green.
2. **build** — needs test. `pip install build`; `python -m build`; assert built version == `github.event.release.tag_name` (no dev suffix). Upload `dist/` as a workflow artifact.
3. **testpypi** — needs build. **No source checkout** — only `download-artifact` into `dist/`, then publish. `pypa/gh-action-pypi-publish@release/v1` with `repository-url: https://test.pypi.org/legacy/`, `skip-existing: true`, `continue-on-error: true` (non-blocking). `environment: testpypi`, `permissions: id-token: write`.
4. **pypi** — needs build (NOT gated on testpypi). **No source checkout** — only `download-artifact` into `dist/`, then publish. `pypa/gh-action-pypi-publish@release/v1` to PyPI; `attestations: true` (default — leave it on, uploads PEP 740 attestations). `environment: pypi`, `permissions: id-token: write`.
5. **github-release** — needs pypi. Download the `dist/` artifact; `gh release upload ${{ github.event.release.tag_name }} dist/*`. `permissions: contents: write`. Release notes untouched (whatever `--generate-notes` produced).
6. **docs** — needs pypi. `hatch run docs:deploy --force` (`mkdocs gh-deploy`). `permissions: contents: write`.

## One-time manual setup (out of band)

Documented in a `RELEASING.md`; the human performs these:

- **PyPI Trusted Publisher** at pypi.org: owner `d-v-b`, repo `pydantic-bigstitcher`, workflow `release.yml`, environment `pypi`.
- **TestPyPI Trusted Publisher** at test.pypi.org: same, environment `testpypi`.
- **GitHub Environments** `pypi` and `testpypi` (optional protection rules / required reviewers).
- **Enable GitHub Pages** (source: `gh-pages` branch) — currently `has_pages: false` and no `gh-pages` branch exists; `gh-deploy` creates the branch but Pages must be turned on for the site to serve.

## Release procedure (going forward)

```
gh release create v0.0.11 --generate-notes --title "v0.0.11"
```

This creates the tag + release, firing `release.yml`: test → build → TestPyPI (non-blocking)
→ PyPI → attach artifacts → deploy docs. No `__about__.py` edit, no `hatch publish`, no tokens.

## Deliverables (all on `add-release-workflow`)

- `pyproject.toml` — hatch-vcs build system + version source; coverage omit cleanup.
- Delete `src/pydantic_bigstitcher/__about__.py`.
- `src/pydantic_bigstitcher/__init__.py` — `importlib.metadata` version.
- `.github/workflows/test.yml` — add `workflow_call`.
- `.github/workflows/release.yml` — new.
- `RELEASING.md` — procedure + one-time setup checklist.

## Out of scope

- Separate `sigstore/gh-action-sigstore-python` job (PEP 740 attestations are kept via the publish action's default — see Decisions).
- SHA-pinning of actions (using major-version tags + Dependabot instead).
- Automated version bump commits (hatch-vcs makes them unnecessary).
- Changelog automation beyond GitHub's `--generate-notes`.

## Best-practices alignment (PyPA, verified 2026-05-29)

Checked against the PyPA guide "Publishing package distribution releases using GitHub
Actions CI/CD workflows" and `pypa/gh-action-pypi-publish` docs:

- Trusted Publishing (OIDC, no tokens) — recommended approach. ✓
- Separate build vs. publish jobs — recommended. ✓
- Artifact upload/download between jobs — recommended. ✓
- Per-job `id-token: write` scoped to publish jobs — recommended. ✓
- Dedicated GitHub Environments (`pypi`/`testpypi`) — recommended. ✓
- TestPyPI first — recommended. ✓
- **Publish jobs do no source checkout** (download-artifact only, minimal attack
  surface) — recommended; encoded above. ✓
- **PEP 740 attestations on by default** — kept (no extra cost). ✓
