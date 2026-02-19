"""Unit test file for team _z"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 
import random


class TestTeam__z(unittest.TestCase):
    """Test team _z PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_th_tnin(self):
        """Test TH_TNIN functionality"""
        sec1 = [str(random.randint(0,2)) for _ in range(3)]
        sec2 = ['2345', '3456', '4567']
        sec3 = [''.join(str(random.randint(0,9)) for _ in range(5)) for _ in range(3)]
        sec4 = [''.join(str(random.randint(0,9)) for _ in range(2)) for _ in range(3)]
        sec5 = [str(random.randint(0,9)) for _ in range(3)]
        ivprovinces = ["28", "29", "59", "68", "69", "78", "79", "87", "88", "89", "97", "98", "99"]
        for i in sec1:
            for w in sec2:
                for x in sec3:
                    for y in sec4:
                        for z in sec5:
                            idnum = f"{i}{w}{x}{y}{z}"
                            known_valid_tnin = "1101700203451"
                            result = analyze_text(f"My Thai ID number is {known_valid_tnin}",["TH_TNIN"])
                            print(result)
                            is_invalid = False
                        
                            if len(idnum) != 13 or not idnum.isdigit():
                               is_invalid = True
                            elif idnum[0] =='0' or idnum[1] == '0':
                               is_invalid = True
                            if is_invalid :
                                self.assertFalse(result, f"Invalid TNIN recognized: {idnum}")

                            else:
                                self.assertTrue(result, f"Invalid TNIN recognized: {idnum}")
                                self.assertEqual(result[0].entity_type, 'TH_TNIN')
                                self.assertAlmostEqual(result[0].score,1.0,2)
                            # else:
                            #     self.fail(f"Valid TNIN not recognized: {idnum}")
                            # # if is_invalid:
                            # #     self.assertFalse(result)
                            # # else:
                            # #     self.assertTrue(result)
                           
                         
                           
                            

        #[type: TH_TNIN, start: 21, end: 34, score: 1.0]
    def test_kr_rrn(self):
        """Test KR_RRN functionality"""

    def test_in_gstin(self):
        """Test IN_GSTIN functionality"""

    def test_sg_nric_fin(self):
        """Test SG_NRIC_FIN functionality"""

    def test_sg_uen(self):
        """Test SG_UEN functionality"""


if __name__ == '__main__':
    unittest.main()
