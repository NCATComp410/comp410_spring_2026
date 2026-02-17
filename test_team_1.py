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

        # Positive case 1
        text1 = "My passport number is A1234567."
        results1 = analyze_text(text1, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results1), results1

        # Positive case 2
        text2 = "Indian Passport No: Z7654321 for travel."
        results2 = analyze_text(text2, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results2), results2

        # Positive case 3
        text3 = "Passport No. B1234567 is listed on the form."
        results3 = analyze_text(text3, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results3), results3

        # Negative case (same format but no passport context)
        text4 = "Reference code AB1234567 was used for shipment."
        results4 = analyze_text(text4, entity_list)
        assert not any(r.entity_type == "IN_PASSPORT" for r in results4), results4

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
