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

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""
        entity_list = ["IN_VEHICLE_REGISTRATION"]

        # Positive case 1: Standard Delhi Private Vehicle (DL = Delhi)
        text1 = "The car registration number is DL 10 CJ 1234."
        results1 = analyze_text(text1, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results1), 
                        f"Failed to detect valid Delhi plate in: {text1}")

        # Positive case 2: Maharashtra Commercial Plate (MH = Maharashtra)
        text2 = "Please log the vehicle plate MH 12 AB 5678 for the permit."
        results2 = analyze_text(text2, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results2), 
                        f"Failed to detect valid Maharashtra plate in: {text2}")

        # Positive case 3: Karnataka registration (KA = Karnataka)
        text3 = "The suspect was driving a vehicle with registration KA 01 MG 9999."
        results3 = analyze_text(text3, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results3), 
                        f"Failed to detect valid Karnataka plate in: {text3}")

        # Negative case
        # 'ZZ' is not a valid Indian State Code, so the pattern match should fail.
        text4 = "Internal warehouse bin location is ZZ 99 XX 0000."
        results4 = analyze_text(text4, entity_list)
        self.assertFalse(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results4), 
                         f"False positive detected for invalid state code in: {text4}")
        
    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
