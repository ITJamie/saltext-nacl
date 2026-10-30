# Maintenance and release checklist

This repository is independently hosted under **ITJamie**. No Salt Extensions
organization repository request has been submitted. No first release is authorized.

## Prepared GitHub configuration

- Public repository, default branch `main`.
- GitHub Pages deploys built documentation from Actions, using `github-pages`.
- Package publication uses the `release` environment and OIDC Trusted Publishing.
- `ENABLE_PYPI_PUBLISH` must remain **`false`** until a release is deliberately approved.
- `PUBLISH_INDEX` defaults to **`testpypi`**. Production publishing requires explicitly
  setting it to `pypi` and deliberately dispatching the publish workflow.
- Release preparation opens an ordinary PR; merging it does not create a tag or publish.
  This works with the default GitHub token, with no GitHub App/private key required.

## Account-side Trusted Publisher setup (not performed)

Create pending publishers separately on PyPI and TestPyPI with these exact values:

| Field | Value |
| --- | --- |
| PyPI project name | `saltext.nacl` |
| GitHub owner | `ITJamie` |
| GitHub repository | `saltext-nacl` |
| Workflow filename | `deploy-package-action.yml` |
| Environment name | `release` |

Use https://pypi.org/manage/account/publishing/ and
https://test.pypi.org/manage/account/publishing/. No API token is needed.
Do not register publishers or upload packages as part of repository preparation.

## Before a future release

- [ ] Review all CI results, including every OS/Python job and installed-wheel smoke test.
- [ ] Confirm 100% extension line and branch coverage and passing strict docs/lint/security checks.
- [ ] Test the wheel with a staging Salt onedir master and relevant minions.
- [ ] Check existing ciphertext and key/config compatibility; back up original keys.
- [ ] Review PyNaCl/libsodium changes and security reports.
- [ ] Register the pending Trusted Publishers under the appropriate account.
- [ ] Dispatch **Prepare release** with a SemVer version (for example `1.0.0`).
- [ ] Review the generated changelog PR, rerun CI if the bot PR did not trigger it,
      and merge only after review.
- [ ] Create and push an annotated or signed `v<version>` tag at the reviewed `main` commit.
      The tag workflow builds/validates artifacts but does not publish them.
- [ ] Enable `ENABLE_PYPI_PUBLISH`, choose `PUBLISH_INDEX=testpypi`, and manually dispatch
      **Publish package** with the validated tag. Confirm installation from TestPyPI.
- [ ] Deliberately switch `PUBLISH_INDEX=pypi` and dispatch for production only when ready.
- [ ] Publish the GitHub release with the exact verified artifacts; verify docs and package metadata.
- [ ] Reset `ENABLE_PYPI_PUBLISH=false` after publishing.

Never tag or publish a version merely to exercise CI. Main-branch CI produces
wheel/source-distribution and documentation artifacts without a release.

## Keeping the project current

Review dependencies, supported Salt point releases and Python/OS runners regularly.
The template was pinned to `0.10.0`; review our documented overrides before a Copier update.
Security fixes, releases and support decisions remain the maintainer's responsibility.
