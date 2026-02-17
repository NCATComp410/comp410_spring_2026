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

        valids = ['234567890124', '345678901238', '456789012341']
        invalids = ['123456789012', '12d3984D03', '234567843429012', '123456654321'] # Invalid codes if you want to try them

        for a in valids:
            result = analyze_text(f"My Uidai number is {a}", ['IN_AADHAAR'])

            if a[0] == '1' or a[0] == '0':
                # Negative case (invalid starting number)
                self.assertFalse(result, "AADHAAR should not start with 0 or 1")

            else:
                # Positive cases
                self.assertTrue(result, "AADHAAR number not being picked up, check the regex pattern or context words "
                "(likely a verhoeff checksum issue if you picked the number yourself)")
                self.assertEqual(result[0].entity_type, 'IN_AADHAAR')
                
                # We can set the approximation test to 1.0 since the context boosters are particular (UIDAI and AADHAAR)
                # [type: IN_AADHAAR, start: 19, end: 31, score: 1.0]
                self.assertAlmostEqual(result[0].score, 1.0, 2)




    def test_in_pan(self):
        """Test IN_PAN functionality"""

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""

    def test_in_voter(self):
        """Test IN_VOTER functionality"""


if __name__ == '__main__':
    unittest.main()
