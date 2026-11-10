import base64
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


POW_MESSAGE = "Jiaming-Luo57308"


def generate_key_pair():
    """Generate a fresh RSA private key and its corresponding public key."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()


def signature_padding():
    """Use the same RSA-PSS parameters for signing and verification."""
    return padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32)


def sign_message(private_key, message):
    """Sign the original message bytes using RSA-PSS with SHA-256."""
    return private_key.sign(message, signature_padding(), hashes.SHA256())


def verify_signature(public_key, message, signature):
    """Return whether the signature matches the message and public key."""
    try:
        public_key.verify(signature, message, signature_padding(), hashes.SHA256())
    except InvalidSignature:
        return False
    return True


def main():
    message = POW_MESSAGE.encode("utf-8")
    private_key, public_key = generate_key_pair()
    signature = sign_message(private_key, message)

    tampered_message = message + b"!"
    original_verified = verify_signature(public_key, message, signature)
    tampered_verified = verify_signature(public_key, tampered_message, signature)
    signature_base64 = base64.b64encode(signature).decode("ascii")

    print(f"PoW message: {POW_MESSAGE}")
    print(f"PoW SHA-256: {hashlib.sha256(message).hexdigest()}")
    print(f"RSA key pair generated: {public_key.key_size} bits")
    print("Signature scheme: RSA-PSS with SHA-256 and MGF1(SHA-256)")
    print(f"Signature (Base64): {signature_base64}")
    print(f"Original message verified: {original_verified}")
    print(f"Tampered message: {tampered_message.decode('utf-8')}")
    print(f"Tampered message verified: {tampered_verified}")

    return 0 if original_verified and not tampered_verified else 1


if __name__ == "__main__":
    raise SystemExit(main())
