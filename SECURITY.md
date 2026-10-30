# Security

Never attach private keys, decrypted secrets or production configuration to an issue.
For a suspected vulnerability, use this repository's **Security → Report a vulnerability**
(private vulnerability reporting). If unavailable, email the maintainer at
**git@jam.ie**, requesting a private channel before sending sensitive details.
Do not open a public vulnerability report or send production secret material.

Only Salt 3008 is supported. Keep PyNaCl and its bundled libsodium up to date.
The extension preserves existing encryption formats; it does not invent a new cipher.
FIPS restrictions are enforced. Keep private keys on hosts that must decrypt;
share only public keys with people or machines that only need to encrypt.
