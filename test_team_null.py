"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""

    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_t_identity_card(self):
        """Test T_IDENTITY_CARD functionality (ID number + expiration date)"""
        positives = [
            "Customer provided ID: A1234567 exp 12/2027 for verification.",
            "Identity Card # ZX9K21A0 Expires 01/29 (do not log).",
            "Document number: QWERTY99 expiration: 05/2026",
        ]
        negatives = [

            "Order number A1234567 ships 12/2027",
            "My appointment is 12/2027",
            "ID: A1234567 was recorded",
            "Identity Card: A12 exp 12/2027",
        ]
        # Positive tests
        for text in positives:
            result = analyze_text(text, ["T_IDENTITY_CARD"])
            self.assertTrue(result, f"T_IDENTITY_CARD not recognized: {text}")
            self.assertEqual(result[0].entity_type, "T_IDENTITY_CARD")
            self.assertGreaterEqual(result[0].score, 0.80)
        # Negative tests
        for text in negatives:
            result = analyze_text(text, ["T_IDENTITY_CARD"])
            self.assertEqual(len(result), 0, f"False positive T_IDENTITY_CARD: {text}")


if __name__ == '__main__':
    unittest.main()
