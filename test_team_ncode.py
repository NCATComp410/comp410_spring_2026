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

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""
        #Positive test
        valid_email = "john.doe@example.com"
        result = analyze_text(f"My email is {valid_email}", entity_list=['EMAIL_ADDRESS'])
        self.assertTrue(result, f"Email is not recognized {valid_email}")
        self.assertEqual(result[0].entity_type, 'EMAIL_ADDRESS')

        #Negative test    
        invalid_email = "Bob.smith@@localhost"
        result = analyze_text(f"My email is {invalid_email}", entity_list=['EMAIL_ADDRESS'])
        self.assertFalse(result, 'EMAIL_ADDRESS')

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
