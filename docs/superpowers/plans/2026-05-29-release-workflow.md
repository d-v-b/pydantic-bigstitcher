# Release Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the manual PyPI release process with a GitHub Actions workflow that builds and publishes to TestPyPI then PyPI via OIDC Trusted Publishing, gated on tests, triggered by publishing a GitHub Release.

**Architecture:** Switch versioning to `hatch-vcs` (version derived from the git tag). Refactor `test.yml` into a reusable workflow. Add `release.yml` with separate build / publish (TestPyPI, PyPI) / github-release / docs jobs; publish jobs use Trusted Publishing (no tokens) at the top level (not in a reusable workflow), do no source checkout, and keep PEP 740 attestations on by default. Third-party actions are SHA-pinned.

**Tech Stack:** hatchling + hatch-vcs, GitHub Actions, `pypa/gh-action-pypi-publish`, `actions/upload-artifact` / `download-artifact`, mkdocs (gh-deploy), pytest via hatch.

**Spec:** `docs/superpowers/specs/2026-05-29-release-workflow-design.md`

**Worktree:** All work happens in a worktree at `../pbs-release` on branch `add-release-workflow` (created at execution start via the using-git-worktrees skill). Paths below are relative to the repo root inside that worktree.

**Action SHAs (pin these exact values — verify/update at execution time, Dependabot will bump later):**

- `actions/checkout@v6` → resolve to current v6 SHA
- `actions/setup-python@v6` → resolve to current v6 SHA
- `actions/upload-artifact@v4` → resolve to current v4 SHA
- `actions/download-artifact@v4` → resolve to current v4 SHA
- `pypa/gh-action-pypi-publish@release/v1` → resolve to current release/v1 SHA (must be ≥ v1.11.0 for default attestations)

> **Pinning note:** Each step below shows the action with its `@<tag>` for readability and a trailing `# <tag>` comment. When writing the real files, replace `<tag>` with the resolved 40-char commit SHA and keep the `# <tag>` comment so Dependabot and humans can read it. Resolve a SHA with:
> `gh api repos/actions/checkout/git/refs/tags/v6 --jq .object.sha` (and analogously for the others; for `pypa/gh-action-pypi-publish` use `git/refs/heads/release/v1`).

---

### Task 1: Switch build backend to hatch-vcs

**Files:**

- Modify: `pyproject.toml` (build-system, version source, coverage omit)
- Delete: `src/pydantic_bigstitcher/__about__.py`

- [ ] **Step 1: Update the build-system requires**

In `pyproject.toml`, change the `[build-system]` table from:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

to:

```toml
[build-system]
requires = ["hatchling", "hatch-vcs"]
build-backend = "hatchling.build"
```

- [ ] **Step 2: Change the version source to vcs**

In `pyproject.toml`, replace:

```toml
[tool.hatch.version]
path = "src/pydantic_bigstitcher/__about__.py"
```

with:

```toml
[tool.hatch.version]
source = "vcs"
```

- [ ] **Step 3: Remove the stale coverage omit**

In `pyproject.toml`, in `[tool.coverage.run]`, change:

```toml
omit = [
  "src/pydantic_bigstitcher/__about__.py",
]
```

to:

```toml
omit = []
```

- [ ] **Step 4: Delete the old version file**

Run: `git rm src/pydantic_bigstitcher/__about__.py`
Expected: `rm 'src/pydantic_bigstitcher/__about__.py'`

- [ ] **Step 5: Verify hatch-vcs resolves the version from git**

Run: `pip install hatch hatch-vcs && hatch version`
Expected: prints a version derived from git (e.g. `0.0.11.devN+g<sha>` since HEAD is past v0.0.10 and untagged). A `dev` suffix here is correct — it confirms hatch-vcs is reading git. It will resolve to a clean `0.0.11` only when built from the `v0.0.11` tag.

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml
git commit -m "build: switch versioning to hatch-vcs"
```

---

### Task 2: Expose runtime **version** via importlib.metadata

**Files:**

- Modify: `src/pydantic_bigstitcher/__init__.py`
- Test: `tests/test_version.py` (create)

- [ ] **Step 1: Write the failing test**

Create `tests/test_version.py`:

```python
import re

import pydantic_bigstitcher


def test_version_is_exposed():
    assert isinstance(pydantic_bigstitcher.__version__, str)
    # PEP 440-ish: at least N.N.N, possibly with a dev/local suffix
    assert re.match(r"^\d+\.\d+\.\d+", pydantic_bigstitcher.__version__)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `hatch env run --env test.py3.12 run tests/test_version.py`
Expected: FAIL — `AttributeError: module 'pydantic_bigstitcher' has no attribute '__version__'`

- [ ] **Step 3: Add the version export**

In `src/pydantic_bigstitcher/__init__.py`, after the existing import line `from pydantic_bigstitcher.core import *  # noqa`, add:

```python
from importlib.metadata import version

__version__ = version("pydantic-bigstitcher")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `hatch env run --env test.py3.12 run tests/test_version.py`
Expected: PASS

(The package must be installed in the env for `importlib.metadata` to find it — hatch installs the project into its envs by default, so this works. If run outside hatch, `pip install -e .` first.)

- [ ] **Step 5: Commit**

```bash
git add src/pydantic_bigstitcher/__init__.py tests/test_version.py
git commit -m "feat: expose __version__ via importlib.metadata"
```

---

### Task 3: Make test.yml a reusable workflow

**Files:**

- Modify: `.github/workflows/test.yml`

- [ ] **Step 1: Add workflow_call to the triggers**

In `.github/workflows/test.yml`, change the `on:` block from:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

to:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
  workflow_call:
```

- [ ] **Step 2: SHA-pin the actions already used in test.yml**

In `.github/workflows/test.yml`, replace `uses: actions/checkout@v6` with the SHA-pinned form (keep tag in a trailing comment):

```yaml
- uses: actions/checkout@<sha> # v6
```

and replace `uses: actions/setup-python@v6` with:

```yaml
- name: Set up Python
  uses: actions/setup-python@<sha> # v6
```

Resolve each `<sha>` per the Action SHAs note at the top of this plan.

- [ ] **Step 3: Validate the workflow YAML**

Run: `python -c "import yaml,sys; yaml.safe_load(open('.github/workflows/test.yml')); print('ok')"`
Expected: `ok`

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/test.yml
git commit -m "ci: make test workflow reusable (workflow_call) and pin actions"
```

---

### Task 4: Add the release workflow

**Files:**

- Create: `.github/workflows/release.yml`

- [ ] **Step 1: Create the release workflow**

Create `.github/workflows/release.yml` with the following content. Replace every `@<sha>  # <tag>` with the resolved SHA (see top-of-plan note); keep the trailing tag comment.

```yaml
name: Release

on:
  release:
    types: [published]

permissions: {}

jobs:
  test:
    uses: ./.github/workflows/test.yml

  build:
    needs: test
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@<sha> # v6
        with:
          fetch-depth: 0 # hatch-vcs needs tags to compute the version
      - name: Set up Python
        uses: actions/setup-python@<sha> # v6
        with:
          python-version: "3.12"
      - name: Build distributions
        run: |
          python -m pip install --upgrade pip build
          python -m build
      - name: Assert built version matches the release tag
        env:
          TAG: ${{ github.event.release.tag_name }}
        run: |
          expected="${TAG#v}"
          echo "Release tag: $TAG -> expected version: $expected"
          ls dist/
          # every wheel/sdist filename must contain the exact expected version
          for f in dist/*; do
            case "$(basename "$f")" in
              pydantic_bigstitcher-"$expected"-*|pydantic_bigstitcher-"$expected".tar.gz) ;;
              *) echo "ERROR: $f does not match version $expected (dirty/untagged build?)"; exit 1 ;;
            esac
          done
      - name: Upload distributions artifact
        uses: actions/upload-artifact@<sha> # v4
        with:
          name: python-package-distributions
          path: dist/

  testpypi:
    needs: build
    runs-on: ubuntu-latest
    continue-on-error: true
    environment: testpypi
    permissions:
      id-token: write
    steps:
      - name: Download distributions
        uses: actions/download-artifact@<sha> # v4
        with:
          name: python-package-distributions
          path: dist/
      - name: Publish to TestPyPI
        uses: pypa/gh-action-pypi-publish@<sha> # release/v1
        with:
          repository-url: https://test.pypi.org/legacy/
          skip-existing: true

  pypi:
    needs: build
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      id-token: write
    steps:
      - name: Download distributions
        uses: actions/download-artifact@<sha> # v4
        with:
          name: python-package-distributions
          path: dist/
      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@<sha> # release/v1

  github-release:
    needs: pypi
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Download distributions
        uses: actions/download-artifact@<sha> # v4
        with:
          name: python-package-distributions
          path: dist/
      - name: Attach artifacts to the GitHub Release
        env:
          GH_TOKEN: ${{ github.token }}
          TAG: ${{ github.event.release.tag_name }}
        run: gh release upload "$TAG" dist/* --repo "$GITHUB_REPOSITORY"

  docs:
    needs: pypi
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@<sha> # v6
        with:
          fetch-depth: 0
      - name: Set up Python
        uses: actions/setup-python@<sha> # v6
        with:
          python-version: "3.12"
      - name: Deploy docs
        run: |
          python -m pip install --upgrade pip hatch
          hatch run docs:deploy --force
```

- [ ] **Step 2: Validate the workflow YAML**

Run: `python -c "import yaml; yaml.safe_load(open('.github/workflows/release.yml')); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Lint with actionlint (if available)**

Run: `actionlint .github/workflows/release.yml || echo "actionlint not installed — skip"`
Expected: no errors (or the skip message). Note: actionlint may warn that the `attestations` behavior is implicit — that's expected; attestations are on by default for Trusted Publishing.

- [ ] **Step 4: Confirm no SHA placeholders remain**

Run: `grep -n "@<sha>" .github/workflows/release.yml && echo "PLACEHOLDERS REMAIN — fix" || echo "no placeholders"`
Expected: `no placeholders`

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/release.yml
git commit -m "ci: add release workflow with PyPI trusted publishing"
```

---

### Task 5: Add RELEASING.md

**Files:**

- Create: `RELEASING.md`

- [ ] **Step 1: Create the release documentation**

Create `RELEASING.md`:

````markdown
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
````

- [ ] **Step 2: Run pre-commit on the new file**

Run: `pre-commit run --files RELEASING.md`
Expected: hooks pass (blacken-docs/prettier may reformat — re-stage if so).

- [ ] **Step 3: Commit**

```bash
git add RELEASING.md
git commit -m "docs: add RELEASING guide"
```

---

### Task 6: Verify the full build end-to-end locally

**Files:** none (verification only)

- [ ] **Step 1: Build from a temporary local tag to confirm a clean version**

```bash
git tag -d _verify 2>/dev/null || true
git tag _verify
HATCH_VCS_PRETEND_VERSION= python -m build 2>/dev/null || python -m build
ls dist/
git tag -d _verify
```

Expected: `dist/` contains `pydantic_bigstitcher-<version>-py3-none-any.whl` and a matching `.tar.gz`. (The version reflects the latest reachable tag; the point is a clean, non-dirty build succeeds.)

> Note: this is a local sanity check only. Do NOT push `_verify`. Clean `dist/` afterward if desired (it is gitignored).

- [ ] **Step 2: Run the full test suite once**

Run: `hatch run test.py3.12:run`
Expected: all tests pass, including `tests/test_version.py`.

- [ ] **Step 3: Confirm clean working tree**

Run: `git status --short`
Expected: no tracked changes (only untracked `dist/` / local noise).

---

## Self-Review

**Spec coverage:**

- hatch-vcs build system + version source + coverage cleanup → Task 1 ✓
- Delete `__about__.py` → Task 1 ✓
- `importlib.metadata` runtime version → Task 2 ✓
- test.yml `workflow_call` → Task 3 ✓
- `release.yml` job graph (test → build → testpypi → pypi → github-release → docs) → Task 4 ✓
- Version guard (built version == tag) → Task 4, build job "Assert" step ✓
- TestPyPI non-blocking (`continue-on-error`, `skip-existing`) → Task 4 ✓
- Publish jobs do no source checkout (download-artifact only) → Task 4 ✓
- PEP 740 attestations kept (no `attestations: false`) → Task 4 (pypi job has no override) ✓
- SHA-pinned actions → top-of-plan note + applied in Tasks 3 & 4 ✓
- Trusted Publishing NOT inside reusable workflow → Task 4 (publish jobs are top-level) ✓
- RELEASING.md with one-time setup incl. pypi manual approval → Task 5 ✓

**Out-of-band items (cannot be done in code — documented in RELEASING.md, human performs):**
PyPI/TestPyPI trusted publishers, GitHub Environments + `pypi` required reviewer, enabling Pages.

**Placeholder scan:** The only intentional placeholders are `@<sha>` action pins, with an explicit resolution command and a Task 4 grep gate that fails if any remain. No TODO/TBD content.

**Type/name consistency:** artifact name `python-package-distributions` is identical across build/testpypi/pypi/github-release jobs. `__version__` attribute name consistent between Task 2 implementation and test.
