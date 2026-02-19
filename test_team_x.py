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
        #Positive tests
        #City
        results = analyze_text("John lives in Houston", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0)
        #Country
        results = analyze_text("Maria is visiting Canada", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0)
        #State
        results = analyze_text("They moved to California", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0) 

        #Negative test
        results = analyze_text("Billy likes pizza", ["LOCATION"])
        print(results)
        self.assertEqual(len(results), 0)

    def test_person(self):
        """Test PERSON functionality"""
        results = analyze_text("Alice and Bob went to school", ["PERSON"])
        self.assertTrue(
            any(r.entity_type == "PERSON" for r in results),
            msg="Failed to detect PERSON entity"
        )

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
