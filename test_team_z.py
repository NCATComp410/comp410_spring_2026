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
        # format is [STGFM][0-9]{7}[A-Z]
        prefix = ['S', 'T', 'G', 'F','M','A'] #first letter acceptable - except A
        mid = ['1234567' , '9876543','123456'] # 7 digits - 6 digits would not be accepted 
        suffix = ['D','A','Z','K'] # last letter of ID

        # loop through all combinations 
        for p in prefix: # the starting letter of NRIC/FIN
            for m in mid: # the 7 digit sequence
                for s in suffix: # the last letter of the ID
                    result = analyze_text(f'My NRIC is {p}{m}{s}', ['SG_NRIC_FIN'])

                    if p not in ['S', 'T','G','F','M']:
                        # negative testcase : with A not being a valid starting letter 
                        if result: # needed for weak pattern w/ low or med confidence
                            self.assertLess(result[0].score, 0.7, 
                                            f'Invalid prefix should not have high confidence: {p}{m}{s}')
                        else:    
                            self.assertFalse(result)
                    elif len(m) != 7:
                        # negative testcase : the sequence must be exactly 7 digits 
                        self.assertFalse(result)
                    else: 
                        # positive test cases 
                        self.assertTrue(result, f'NRIC not recongized {p}{m}{s}')
                        self.assertEqual(result[0].entity_type, 'SG_NRIC_FIN')
                        self.assertGreaterEqual(result[0].score, 0.5)

    def test_sg_uen(self):
        """Test SG_UEN functionality"""


if __name__ == '__main__':
    unittest.main()
