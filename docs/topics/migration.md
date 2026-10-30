# Migration from core NaCl

The core cleanup removed the runner and external pillar but retained the execution
module, renderer and utility. This extension supplies all five and preserves public
`nacl.*` names, `nacl.config`, base64 key files, ciphertext and legacy arguments.
The source and separate fixes are recorded in [PROVENANCE](https://github.com/ITJamie/saltext-nacl/blob/main/PROVENANCE.md).

1. Back up keys and configuration securely. Do not generate replacement keys.
2. Remove any temporary custom `nacl` runner copies or custom loader-directory overrides;
   they can shadow an installed extension. Preserve unrelated custom plugins.
3. Install the wheel into Salt's own environment on the master and relevant minions.
4. Restart affected daemons, then encrypt and decrypt a new test value with the existing keys.
5. Verify an existing encrypted value, renderer SLS and external pillar compilation in staging.

Salt discovers the extension through `salt.loader`; its modules take precedence over
retained core versions. The wheel tests assert the four plugin loader origins, not just names.
Salt intentionally disables extension lookup in its utilities loader, so the
shared utility is an ordinary namespaced Python import, also checked by the tests.
Shared helpers are imported from `saltext.nacl.utils`, never core `salt.utils.nacl`.
Salt's existing NaCl native-library import hook remains in Salt; this package adds no hook.

Rolling back means uninstalling the extension and restarting affected daemons. Core
3008 still lacks its runner and external pillar, so arrange a tested fallback before rollback.
