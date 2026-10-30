# Installation and compatibility

Supported: Salt **3008**, Python **3.10+**, PyNaCl **1.6.2+**. CI uses Salt 3008.5.
There is no released package on PyPI yet. Download the wheel artifact from a
successful GitHub Actions CI run and install it with `salt-pip install /path/to/file.whl`,
or use `salt-pip install 'git+https://github.com/ITJamie/saltext-nacl.git@main'`.
The version of a source build is an unreleased development version from Git.

Install into the Python environment used by Salt, not an unrelated system pip.
Master: required for runners, external pillar and master-side pillar rendering.
Minions: required on each host using NaCl execution functions or local rendering.
Restart the affected master/minion after an install or upgrade. `salt-run` is a
new process per invocation. `saltutil.sync_all` does not distribute pip packages.

The regular extension installation depends on PyNaCl, not Salt itself, to avoid
replacing a packaged Salt installation. For a fresh system/virtualenv installation,
`python -m pip install '.[salt]'` additionally installs Salt 3008.

Once an initial PyPI release exists, the normal command will be
`salt-pip install saltext.nacl`. That command is not an installation path today.
