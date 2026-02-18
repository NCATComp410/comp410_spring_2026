"""Unit test file for team ncode"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_ncode(unittest.TestCase):
    """Test team ncode PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""
        # Positive test - Bitcoin-like wallet format
        valid_wallet = "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
        result = analyze_text(
            valid_wallet,
            entity_list=['CRYPTO']
        )

        self.assertTrue(result, f"CRYPTO not recognized {valid_wallet}")
        self.assertEqual(result[0].entity_type, 'CRYPTO')

        # Negative test
        normal_text = "This is normal text with no secrets."
        result = analyze_text(
            normal_text,
            entity_list=['CRYPTO']
        )

        self.assertFalse(result, "False positive detected for CRYPTO")


    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
