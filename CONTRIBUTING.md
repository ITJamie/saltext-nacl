# Contributing

Use Python 3.10–3.14. The package targets Salt 3008 only.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install 'salt==3008.5'
python -m pip install -e '.[tests,docs,dev]'
nox -s tests lint docs build
```

CI installs Salt without its broad optional integration dependencies, then
installs the narrow runtime dependencies declared by our `tests` extra. This
avoids requiring unrelated integrations such as MSSQL while exercising real
Salt loaders and CLIs. To reproduce that setup use
`python -m pip install --no-deps salt==3008.5` before installing this project's extras.

Tests use `pytest-salt-factories`, `unittest.mock` and temporary generated keys.
They must not use production keys or Salt's repository-only test helpers.
`python tools/test.py` runs fresh line/branch coverage including subprocesses
and fails unless every runtime line and branch in the extension is covered.
Salt's existing `NaclImporter` is tested as a dependency, not copied or included
in the extension's coverage denominator. No extension-owned behavior is excluded.

The CI matrix covers Linux on Python 3.10–3.14, and Windows/macOS on 3.10 and 3.14.
Windows permission branches are additionally tested with mocks on other systems.
Test Salt configurations set `skip_grains: true`: NaCl does not depend on host
hardware or DNS discovery, which can stall on hosted macOS VMs. This changes
only test configuration, not extension defaults; the real CLI, default runner
job caching and all encryption/decryption assertions remain enabled.
Functional tests verify built-in core NaCl modules lose to the installed extension.
A separate wheel smoke test runs outside the checkout and checks its installation path.

Use a `changelog/<PR number>.added.md`, `.fixed.md` or `.changed.md` fragment.
Keep code cleanup and behavior corrections separate. Preserve the source
attribution and Apache-2.0 notices. Run `pre-commit install` to enable local hooks.

Copier base: official tag `0.10.0`. `.copier-answers.yml` records its real inputs.
Before updating, create a branch, read the template diff, and preserve our
custom packaging, release guards, strict coverage and workflow configuration.
Never update from a nonexistent template version or blindly overwrite overrides.

Do not publish a release simply to test CI. See the release checklist.
