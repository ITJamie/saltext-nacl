# Configuration and use

## Master configuration

Put the following only in `/etc/salt/master.d/nacl.conf`:

```yaml
nacl.config:
  sk_file: /etc/salt/pki/master/nacl_sk
  pk_file: /etc/salt/pki/master/nacl_pk
```

For a new deployment, generate the files once:

```sh
salt-run nacl.keygen sk_file=/etc/salt/pki/master/nacl_sk pk_file=/etc/salt/pki/master/nacl_pk
salt-run nacl.enc data='test'
salt-run nacl.dec data='<encrypted value>'
```

Configuration-only paths are sufficient; no key arguments are needed for `enc`/`dec`.
Explicit key arguments override configuration. Execution functions use Salt's
`config.get` (including its pillar/config precedence); runners fall back to master options.
The default is sealedbox: encrypt with the public key, decrypt with the private key.
Secretbox uses the same secret key in both directions. Existing legacy `key` and
`keyfile` arguments retain their secretbox compatibility behavior.

## Execution module and file helpers

```sh
salt-call --local nacl.enc data='test' pk_file=/path/to/public-key
salt-run nacl.enc_file name=/path/to/plain out=/path/to/encrypted
salt-run nacl.dec_file name=/path/to/encrypted out=/path/to/plain-restored
```

`salt-call` reads minion configuration, not `master.d`; supply a public-key path
or configure the minion separately. File helpers refuse to overwrite an existing output.
New POSIX private-key files are mode `0600`; Windows uses owner/ACL restrictions.

## Pillar renderer

Use `#!yaml|nacl` at the top of a pillar SLS, and wrap encrypted values as
`NACL[<ciphertext>]`. The renderer handles nested mappings/lists and readable inputs.

## External pillar

Place NaCl last in `ext_pillar` so it decrypts values accumulated by earlier sources:

```yaml
ext_pillar:
  - nacl: {}
```

The runner, execution module, utility and external pillar enforce their existing
FIPS restrictions. Do not use NaCl on FIPS-enabled hosts.
