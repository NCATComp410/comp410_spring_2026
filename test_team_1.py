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

    def test_in_voter(self):
        """Test IN_VOTER functionality"""
        # first 3 characters of IN_VOTER
        prefix = ["AAA", "GHJ", "333", "3A4"] # first part of IN_VOTER
        # last 7 digits of IN_VOTER
        suffix = ["1234567", "2348764", "5703067","4570274"] # second part of IN_VOTER

        # iterate through the prefix and suffix test cases
        for p in prefix:
            for s in suffix:

                result = analyze_text(f"My IN_Voter is {p}{s}", ['IN_VOTER'])
                
                # negative test case, first 3 characters need to be alphabetical
                if p == "333" or p == "3A4":
                    self.assertFalse(result)
                else:
                     # positive test cases
                    self.assertTrue(result,f"IN_VOTER not recognized{p}{s}")
                    self.assertEqual(result[0].entity_type, "IN_VOTER")
                    self.assertAlmostEqual(result[0].score, 0.75,2)


if __name__ == '__main__':
    unittest.main()
