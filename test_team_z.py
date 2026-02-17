"""Unit test file for team _z"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__z(unittest.TestCase):
    """Test team _z PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_th_tnin(self):
        """Test TH_TNIN functionality"""

    def test_kr_rrn(self):
        """Test KR_RRN functionality"""

    def test_in_gstin(self):
        """Test IN_GSTIN functionality"""

    def test_sg_nric_fin(self):
        """Test SG_NRIC_FIN functionality"""

    def test_sg_uen(self):
        """Test SG_UEN functionality"""

        prefix = [
            "201912345",   # valid (9 digits)
            "20191234",    # invalid (8 digits)
            "2019ABCDE"    # invalid (non-numeric)
        ]
    
        suffix = [
            "A",  # valid letter
            "Z",  # valid letter
            "1"   # invalid (number)
        ]
    
        # loop through all combinations
        for p in prefix:
            for s in suffix:
                text = f"The company registration number is {p}{s}"
                result = analyze_text(text, ["SG_UEN"])
    
                # negative cases
                if len(p) != 9 or not p.isdigit() or not s.isalpha():
                    self.assertFalse(result)
                else:
                    # positive cases
                    #self.assertEqual(len(result), 1)
                    self.assertEqual(result[0].entity_type, "SG_UEN")
                    self.assertGreaterEqual(result[0].score, 0.5)



if __name__ == '__main__':
    unittest.main()
