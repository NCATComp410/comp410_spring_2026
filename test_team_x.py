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

        # Positive test cases
        valid_numbers = [
            "Call me at 123-456-7890",
            "My number is (123) 456-7890",
            "Reach me at 123 456 7890",
            "Emergency contact: +1 123-456-7890"
        ]

        for text in valid_numbers:
            results = analyze_text(text, ["PHONE_NUMBER"])
            self.assertTrue(
                any(r.entity_type == "PHONE_NUMBER" for r in results),
                msg=f"Failed to detect PHONE_NUMBER in: {text}"
            )

        # Negative test cases
        invalid_numbers = [
            "My code is 123-45-678",
            "Number: 123456789",
            "SSN is 123-45-6789",
            "Random number 987654"
        ]

        for text in invalid_numbers:
            results = analyze_text(text, ["PHONE_NUMBER"])
            self.assertEqual(
                len(results), 0,
                msg=f"Incorrectly detected PHONE_NUMBER in: {text}"
            )


    def test_location(self):
        """Test LOCATION functionality"""

    def test_person(self):
        """Test PERSON functionality"""

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
