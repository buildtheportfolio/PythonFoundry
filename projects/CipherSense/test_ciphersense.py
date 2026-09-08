import math
import unittest

from ciphersense import analyze_password, format_duration


class CipherSenseTests(unittest.TestCase):
    def test_empty_password_is_not_evaluated(self):
        result = analyze_password("")
        self.assertEqual(result.strength, "Not evaluated")
        self.assertEqual(result.score, 0)
        self.assertEqual(result.entropy_bits, 0.0)

    def test_mixed_password_has_multiple_character_domains(self):
        result = analyze_password("Abcd1234!")
        self.assertEqual(result.length, 9)
        self.assertEqual(result.pool_size, 94)
        self.assertGreater(result.entropy_bits, 50)

    def test_common_password_is_flagged(self):
        result = analyze_password("password")
        self.assertTrue(result.common_password)
        self.assertEqual(result.strength, "Critical")

    def test_repetition_and_sequence_are_detected(self):
        repeated = analyze_password("aaaa1111!!!!")
        self.assertTrue(repeated.repeated_pattern)
        sequenced = analyze_password("Qwerty123456")
        self.assertTrue(sequenced.sequence_pattern)
        self.assertTrue(sequenced.keyboard_pattern)

    def test_very_long_random_like_password_scores_high(self):
        result = analyze_password("V7!mQ2#rT9@xK4$pL8^z")
        self.assertGreaterEqual(result.score, 95)
        self.assertGreater(result.effective_entropy_bits, 70)

    def test_invalid_rate_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_password("anything", 0)

    def test_duration_formatter(self):
        self.assertEqual(format_duration(0.5), "less than a second")
        self.assertEqual(format_duration(60), "1.0 minute")
        self.assertTrue(format_duration(math.inf).startswith("effectively infeasible"))


if __name__ == "__main__":
    unittest.main()
