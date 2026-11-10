# Lab 02 — RSA Digital Signatures

## Objective

Generate an RSA key pair, sign the original message from the difficulty-4 Proof of Work result in [Lab 01](../01-proof-of-work/README.md), and verify the signature with the corresponding public key. Reuse the same signature with an altered message to see verification fail.

An RSA digital signature lets someone with the public key check that a signature was produced using the corresponding private key and that it matches the message they received. The signature covers the message bytes. The original message remains readable throughout the demonstration.

## Implementation

1. `generate_key_pair()` generates a fresh 2048-bit RSA private key with public exponent `65537` using `cryptography`. It derives the public key with `private_key.public_key()` and returns both objects. The private key stays in memory during the run. The program never prints it or writes it to a file.
2. `main()` uses the recorded Lab 01 message `Jiaming-Luo57308`, which combines the nickname `Jiaming-Luo` with nonce `57308` without a separator. It encodes the original message as UTF-8. This lab reuses the recorded result directly and does not run the mining search.
3. `sign_message()` passes those bytes to the library, which hashes the message with SHA-256 and applies RSA-PSS with MGF1 using SHA-256 and a 32-byte random salt. The program separately prints the PoW digest for comparison with Lab 01. The input to the signing function is the original message, while the PoW digest is displayed as hexadecimal text.
4. `verify_signature()` passes the public key the original message, signature, and matching PSS parameters. It returns `True` on success and converts `InvalidSignature` to `False`. The demo appends `!` to the message and checks it again with the same signature and public key.

## Install, run, and test

Use Python 3 and run these commands from the repository root. The dependency is listed in `requirements.txt`.

```sh
python -m pip install -r 02-rsa-signature/requirements.txt
python -B 02-rsa-signature/rsa_signature.py
python -B -m unittest discover -s 02-rsa-signature -v
```

## Observed results

The demonstration was run with Python 3.13.7 and `cryptography` 50.0.2.

| Check | Observed result |
| --- | --- |
| Original PoW input | `Jiaming-Luo57308` |
| PoW SHA-256 | `00003a88169ed4efb80491051b09896be3d4c40a7e25cb0111876be8eab89815` |
| Generated RSA key size | 2048 bits |
| Original message verification | `True` |
| Tampered input | `Jiaming-Luo57308!` |
| Tampered message verification with the original signature | `False` |

The program also prints the signature in Base64. Each run generates a new key pair and PSS uses a random salt, so the signature text varies across runs.

All four tests passed. They check the original PoW input and digest, successful verification of the original message, failed verification after changing the message, and failed verification with a different public key.

## Key concepts

- Python strings represent text. `str.encode("utf-8")` produces the bytes used for hashing and signing. `base64.b64encode()` makes the binary signature printable, and `.decode("ascii")` turns the encoded bytes into text. Base64 is a reversible encoding.
- Tuple unpacking assigns the generated private and public keys to separate variables. The `try` and `except` block handles `InvalidSignature`. The `if __name__ == "__main__"` guard lets tests import the functions without running the demonstration.
- SHA-256 produces a fixed-length digest. RSA-PSS combines message hashing with randomized encoding before the RSA signing operation. Signing and verification use the same hash, mask generation function, and salt length. See the [cryptography RSA documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/).
