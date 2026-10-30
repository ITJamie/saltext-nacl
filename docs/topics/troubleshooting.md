# Troubleshooting

- **`nacl.enc` unavailable:** check that the package and PyNaCl are installed in
  the interpreter used by the command. Check FIPS mode and custom loader overrides.
- **`salt-call` cannot find master keys:** it reads minion config; use an explicit
  public-key path for encryption or configure the minion. Never copy private keys unnecessarily.
- **Decryption fails:** verify the matching original keypair and complete ciphertext.
  Do not regenerate keys to resolve an upgrade problem.
- **Wrong implementation loads:** remove old synced/custom NaCl overrides, restart
  daemons, and check `python -m pip show saltext.nacl` using Salt's interpreter.
- **Native library/import crashes:** keep Salt, PyNaCl, libsodium and pyzmq in one
  consistent environment. Do not mix system and onedir site-packages. Include version
  information, not keys or secret values, in an issue.
- **Unclosed Runner warnings:** Salt 3008.5 can emit these even after a successful
  runner operation. The extension does not change Salt's resource cleanup.

Report ordinary bugs at https://github.com/ITJamie/saltext-nacl/issues.
For vulnerabilities use the private reporting channel described in SECURITY.md.
