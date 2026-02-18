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
        prefixes  = ["01", "09", "27", "37"]          # valid state codes
        mids      = ["ABCDE1234F", "QWERT6789Y", "LMNOP4321A", "ZXCVB9876K"]  # PANs
        suffix1s  = ["0", "2", "3", "4"]              # entity numbers
        suffix2s  = ["D"]                             # must be Z
        suffix3s  = ["5", "7", "9", "3"]              # checksums
            
        for prefix in prefixes:
            for mid in mids:
                for suffix1 in suffix1s:
                    for suffix2 in suffix2s:
                        for suffix3 in suffix3s:
                            result = analyze_text(f"My IN_GSTIN is {prefix}{mid}{suffix1}{suffix2}{suffix3}", ["IN_GSTIN"])
                            if suffix2 != 'Z':
                                #negative test cause - has to be Z
                                self.assertFalse(result)
                            else:
                                #positive test cause
                                self.assertTrue(result, f'Entity not found {prefix}{mid}{suffix1}{suffix2}{suffix3}')
                                self.assertEqual(result[0].entity_type, 'IN_GSTIN')
                                self.assertAlmostEqual(result[0].score, 1.0, 2)

    def test_sg_nric_fin(self):
        """Test SG_NRIC_FIN functionality"""

    def test_sg_uen(self):
        """Test SG_UEN functionality"""


if __name__ == '__main__':
    unittest.main()
