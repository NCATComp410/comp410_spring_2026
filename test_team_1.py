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
        entity_list = ["IN_PAN"]

        # positive test case 1
        text1 = "My PAN is ABCDE1234F."
        results1 = analyze_text(text1, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results1), results1)

        # positive test case 2
        text2 = "Permanent Account Number: PQRST6789L"
        results2 = analyze_text(text2, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results2), results2)

        # positive test case 3
        text3 = "pan number is abcdp1234k"
        results3 = analyze_text(text3, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results3), results3)

        # negative case- Incorrect format
        text4 = "PAN: ABCD1234F"
        results4 = analyze_text(text4, entity_list)
        self.assertFalse(any(r.entity_type == "IN_PAN" for r in results4), results4)

        # negative case- invalid structure
        text5 = "PAN: ABCDEFGHIJ"
        results5 = analyze_text(text5, entity_list)
        self.assertFalse(any(r.entity_type == "IN_PAN" for r in results5), results5)
    

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
