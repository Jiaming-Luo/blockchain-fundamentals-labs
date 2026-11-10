import hashlib
import unittest

from rsa_signature import POW_MESSAGE, generate_key_pair, sign_message, verify_signature


class RSASignatureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        private_key, cls.public_key = generate_key_pair()
        cls.message = POW_MESSAGE.encode("utf-8")
        cls.signature = sign_message(private_key, cls.message)

    def test_message_matches_difficulty_four_pow_result(self):
        expected_digest = (
            "00003a88169ed4efb80491051b09896be3d4c40a7e25cb0111876be8eab89815"
        )
        self.assertEqual(self.message, b"Jiaming-Luo57308")
        self.assertEqual(hashlib.sha256(self.message).hexdigest(), expected_digest)

    def test_signature_verifies_for_original_message(self):
        self.assertTrue(verify_signature(self.public_key, self.message, self.signature))

    def test_signature_fails_for_tampered_message(self):
        self.assertFalse(
            verify_signature(self.public_key, self.message + b"!", self.signature)
        )

    def test_signature_fails_for_wrong_public_key(self):
        _, wrong_public_key = generate_key_pair()
        self.assertFalse(verify_signature(wrong_public_key, self.message, self.signature))
