"""Unit test file for team _1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__1(unittest.TestCase):
    """Test team _1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

    def test_in_pan(self):
        """Test IN_PAN functionality"""

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

        entity_list = ["IN_PASSPORT"]

        # Positive case 1: Standard valid passport (no space)
        text1 = "My passport number is A1234567."
        results1 = analyze_text(text1, entity_list)
        self.assertTrue(
            any(r.entity_type == "IN_PASSPORT" for r in results1),
            f"Failed to detect valid passport number in: {text1}"
        )

        # Positive case 2: Valid passport with optional space (matches your regex)
        text2 = "The document shows passport A12 34569 issued in 2018."
        results2 = analyze_text(text2, entity_list)
        self.assertTrue(
            any(r.entity_type == "IN_PASSPORT" for r in results2),
            f"Failed to detect valid spaced passport number in: {text2}"
        )

        # Positive case 3: Another valid pattern with different letter prefix
        text3 = "Passenger ID: K98 76543 was verified at the counter."
        results3 = analyze_text(text3, entity_list)
        self.assertTrue(
            any(r.entity_type == "IN_PASSPORT" for r in results3),
            f"Failed to detect valid passport number in: {text3}"
        )

        # Negative case 1: Wrong format (starts with digit)
        text4 = "The code 91234567 should not be detected as a passport."
        results4 = analyze_text(text4, entity_list)
        self.assertFalse(
            any(r.entity_type == "IN_PASSPORT" for r in results4),
            f"False positive detected for invalid passport format in: {text4}"
        )

        # Negative case 2: Too short / malformed
        text5 = "Temporary ID A12345 is not a passport number."
        results5 = analyze_text(text5, entity_list)
        self.assertFalse(
            any(r.entity_type == "IN_PASSPORT" for r in results5),
            f"False positive detected for short malformed passport in: {text5}"
        )

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
