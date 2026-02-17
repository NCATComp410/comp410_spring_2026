"""Unit test file for team _x"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__x(unittest.TestCase):
    """Test team _x PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""

    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""
        # Positive test cases
        text_with_nhs = "Patient NHS number is 943 476 5919"
        results = analyze_text(text_with_nhs, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertGreater(len(nhs_results), 0, "Should detect NHS number with spaces")
    
        text_no_spaces = "NHS number: 9434765919"
        results = analyze_text(text_no_spaces, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertGreater(len(nhs_results), 0, "Should detect NHS number without spaces")
    
        # Negative test case
        text_invalid = "Patient ID: 123 456 789"  # Only 9 digits
        results = analyze_text(text_invalid, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertEqual(len(nhs_results), 0, "Should not detect invalid NHS number")

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
