"""Unit test file for team 8_ball"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_8_ball(unittest.TestCase):
    """Test team 8_ball PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""
        #ABA Routing number format 
        prefix = ["0110", "0210"] # first 4 numbers 
        mid = ["0001", "0002"] # middle of the numbers 
        suffix = ["5", "1"] #end of the numbers 

        #loop through all combinations
        for p,m,s in zip(prefix,mid,suffix):
            result = analyze_text(f"My ABA Routing Number is {p}-{m}-{s}",['ABA_ROUTING_NUMBER'])
            if m == '0000':
                #negative testcase - 0000 is not valid 
                self.assertFalse(result)
            else: 
                #positive testcase 

                self.assertTrue(result, f'ABA not recongized {p}{m}{s}')
                #[type: ABA_ROUTING_NUMBER, start: 25, end: 34, score: 1.0]\
                self.assertEqual(result[0].entity_type, 'ABA_ROUTING_NUMBER')
                self.assertAlmostEqual(result[0].score, 1.0, 2)

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
