import unittest

from pow import calculate_hash, mine_pow


class ProofOfWorkTests(unittest.TestCase):
    def test_calculate_hash_matches_known_digest(self):
        expected = "56abfbd7d2ea606e667945422de5a368b8b0272b8f29081cb058b594dd7e3249"
        self.assertEqual(calculate_hash("abc", 0), expected)

    def test_mine_pow_returns_first_match(self):
        nonce, hash_value, elapsed, attempts = mine_pow("abc", 2)

        self.assertEqual(nonce, 252)
        self.assertEqual(hash_value, calculate_hash("abc", nonce))
        self.assertTrue(hash_value.startswith("00"))
        self.assertEqual(attempts, 253)
        self.assertGreaterEqual(elapsed, 0)

    def test_zero_difficulty_matches_on_first_attempt(self):
        nonce, hash_value, _, attempts = mine_pow("abc", 0)

        self.assertEqual(nonce, 0)
        self.assertEqual(hash_value, calculate_hash("abc", 0))
        self.assertEqual(attempts, 1)

    def test_rejects_difficulty_outside_hash_length(self):
        for difficulty in (-1, 65):
            with self.subTest(difficulty=difficulty):
                with self.assertRaises(ValueError):
                    mine_pow("abc", difficulty)

    def test_rejects_non_integer_difficulty(self):
        for difficulty in (True, 2.0, "2"):
            with self.subTest(difficulty=difficulty):
                with self.assertRaises(TypeError):
                    mine_pow("abc", difficulty)
