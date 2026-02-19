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

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""

        #positive test case:
        #valid formats
        valid_license = ["AB1234563"]

        for license_str in valid_license:
            result = analyze_text(f"DEA medical certificate number {license_str}", entity_list = ['MEDICAL_LICENSE'])
            self.assertTrue(result, f'MEDICAL_LICENSE not recognized: {license_str}')
            self.assertEqual(result[0].entity_type, 'MEDICAL_LICENSE')

        #negative test case:
        #invalid formats
        invalid_license = ["AB1234567","123456","ABC1234567","ab1234567","A1234567"]
        for invalid_id in invalid_license:
            result = analyze_text(f"DEA medical certificate number {invalid_id}", entity_list = ['MEDICAL_LICENSE'])

            self.assertFalse(result, "False positive detected for MEDICAL_LICENSE")





if __name__ == '__main__':
    unittest.main()
