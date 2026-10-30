# saltext.nacl

NaCl encrypted secrets for **Salt 3008**, maintained by [ITJamie](https://github.com/ITJamie).

[Documentation](https://itjamie.github.io/saltext-nacl/) · [Issues](https://github.com/ITJamie/saltext-nacl/issues)

This self-contained extension supplies the `nacl` execution module, runner,
external pillar, renderer and shared utility. Existing `nacl.*` commands,
`nacl.config` settings, key formats and encrypted values remain compatible.
Python 3.10+ and PyNaCl 1.6.2+ are required. Salt 3006/3007 are not supported.

**Pre-release:** no version tag or PyPI release has been published. Package
publishing is disabled. Use a wheel from a successful CI build, or install
from this repository into Salt's Python environment:

```sh
salt-pip install 'git+https://github.com/ITJamie/saltext-nacl.git@main'
```

Install on the **master** for `salt-run`, pillar rendering and the external
pillar; install on each **minion** that needs the execution module or renderer.
Restart affected daemons after installing or upgrading. For a system/virtualenv
Salt installation, use that interpreter's `python -m pip` instead of `salt-pip`.
Salt is an optional dependency (`.[salt]`); the normal install does not replace it.

Configure only the master, for example `/etc/salt/master.d/nacl.conf`:

```yaml
nacl.config:
  sk_file: /etc/salt/pki/master/nacl_sk
  pk_file: /etc/salt/pki/master/nacl_pk
```

```sh
salt-run nacl.keygen sk_file=/etc/salt/pki/master/nacl_sk pk_file=/etc/salt/pki/master/nacl_pk
salt-run nacl.enc data='test'
# salt-run nacl.dec data='<encrypted value>'
```

Back up existing keys before migrating. Never regenerate keys as an upgrade
step: existing ciphertext needs the original private key. NaCl is unavailable
in FIPS mode. New private-key files use POSIX mode `0600` (Windows uses ACLs).

For development, testing and release preparation see [CONTRIBUTING.md](CONTRIBUTING.md).
For maintenance and publication see [the release checklist](docs/topics/releasing.md).
Source attribution and the pinned Copier template are recorded in [PROVENANCE.md](PROVENANCE.md).
Security reporting is described in [SECURITY.md](SECURITY.md).
