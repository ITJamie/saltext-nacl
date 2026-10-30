# Source provenance

This extension derives from the Apache-2.0 licensed Salt Project:
https://github.com/saltstack/salt

The initial migration uses the five NaCl components from commit
`01252662f9bf9d38cfe81aa9898066632fddf46a` in
https://github.com/saltstack/salt/pull/70621.
Tests are ported from `b47adff3996c2687a9ef7e3fcf231e801e9fd817`.

The unreachable-code removal (`4849aa6d23`) and POSIX permission correction
(`3eebc041f4`) are applied as separate commits after the initial migration.
Salt's NaclImporter remains part of Salt and is tested, not copied or installed again.

Project boilerplate was generated using the official salt-extension-copier
template at tag `0.10.0` (commit `3e9915f1a8f58d33e1a4b631beae9792e764173e`).
The real generation inputs are in `.copier-answers.yml`. Packaging, workflows,
coverage, docs and development commands are deliberately maintained overrides;
review Copier update diffs rather than accepting them blindly.

Preserve LICENSE, NOTICE and this source attribution when redistributing.
Original source contributor history is available at the linked Salt repository.
