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
        mid = ["0001", "0000"] # middle of the numbers 
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

        valid_ids = ["2929 12348 1", "2234 56789 1", "4951 64979 1", "6951 82418 1", "2954 53749 1"]
        #positive test cases for valid ids
        for id in valid_ids:
            result = analyze_text(f"medicare medicare medicare {id}", entity_list = ['AU_MEDICARE'])
            #make sure we get something in the result array
            self.assertTrue(len(result) > 0, "No AU_MEDICARE entity seen")
            self.assertEqual(result[0].entity_type, 'AU_MEDICARE')
            self.assertAlmostEqual(result[0].entity_type, 'AU_MEDICARE')

        #negative test cases for invalid ids
        invalid_ids = ["2234 56789 21", "12345", "2929-12349-1", "ABC D EFG HI", "2929 12338 123", "292912348923"]
        for invalid_id in invalid_ids:
            result = analyze_text(f"My medicare is {invalid_id}", ['AU_MEDICARE'])
            self.assertFalse(result, f"Incorrectly detected invalid Medicare pattern: {invalid_id}")


    def test_au_tfn(self):
        """Test AU_TFN functionality"""


if __name__ == '__main__':
    unittest.main()
