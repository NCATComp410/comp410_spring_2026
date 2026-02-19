"""Unit test file for team _2"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__2(unittest.TestCase):
    """Test team _2 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_it_driver_license(self):
        """Test IT_DRIVER_LICENSE functionality"""
        prefix = ['AA', 'U1'] # one letter
        mid = ['1234567', '7654321', '123456'] # seven alphanumeric characters (negative is 6 characters)
        suffix = ['A', '1'] # one letter

        # loop through all combinations of prefix, mid, and suffix
        for p in prefix:
            for m in mid:
                for s in suffix:
                    result = analyze_text(f"il numero della mia patente è {p}{m}{s}", ["IT_DRIVER_LICENSE"])

                    if m == '123456' or p == 'U1' or s == '1':
                        # negative cases
                        self.assertFalse(result)
                    else:
                        # positive cases
                        self.assertEqual(len(result), 1)
                        self.assertEqual(result[0].entity_type, 'IT_DRIVER_LICENSE')
                        self.assertAlmostEqual(result[0].score, 0.55, 2)

    def test_it_fiscal_code(self):
        """Test IT_FISCAL_CODE functionality"""
        #IT_fiscal_code format
        prefix = ['RSSMRA', 'BNCLRD']   # Surname Name
        mid = ['85M01', '00H00'] # year month date
        suffix = ['H501V', 'G482J'] # Place Control
        # loop through all combinations
        for p in prefix:
            for m in mid:
                for s in suffix:
                    result = analyze_text(f'My IT_fiscal_code {p}{m}{s}', ['IT_FISCAL_CODE'])
                    if m == '00H00':
                        # negative test case - 00H00 is not valid
                        self.assertFalse(result)
                    else:
                        #postive testcase
                        self.assertTrue(result, f'Fiscal_code not Entity not recognized {p}{m}{s}')
                        #[type: IT_FISCAL_CODE, start: 15, end: 31, score: 0.3] 
                        self.assertEqual(result[0].entity_type, 'IT_FISCAL_CODE')
                        self.assertAlmostEqual(result[0].score, 0.3, 2)

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""
        prefix = ['YA', 'AB']
        numbers = ['1234567', '123456'] #7 Digits Valid, 6 Digits Invalid

        for p in prefix:
            for n in numbers:
                result = analyze_text(f'MY IT_passport {p}{n}', ['IT_PASSPORT'])
                if len(n) != 7:
                    self.assertFalse(result)
                else:
                    self.assertTrue(result, f'Passport not recognized {p}{n}')
                    self.assertEqual(result[0].entity_type, 'IT_PASSPORT')
                    self.assertAlmostEqual(result[0].score,0.01,2)
                    
    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
