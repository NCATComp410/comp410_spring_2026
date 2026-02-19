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
        positives = [
            "Customer provided ID: A1234567 exp 12/2027 for verification.",
            "Identity Card # ZX9K21A0 Expires 01/29 (do not log).",
            "Document number: QWERTY99 expiration: 05/2026",
        ]

        negatives = [
          
            "Order number A1234567 ships 12/2027",
            
            "My appointment is 12/2027",
           
            "ID: A1234567 was recorded",
            
            "Identity Card: A12 exp 12/2027",
        ]

        # Positive tests
        for text in positives:
            result = analyze_text(text, ["IT_IDENTITY_CARD"])
            self.assertTrue(result, f"IT_IDENTITY_CARD not recognized: {text}")
            self.assertEqual(result[0].entity_type, "IT_IDENTITY_CARD")
            self.assertGreaterEqual(result[0].score, 0.80)

        # Negative tests
        for text in negatives:
            result = analyze_text(text, ["IT_IDENTITY_CARD"])
            self.assertEqual(len(result), 0, f"False positive IT_IDENTITY_CARD: {text}")

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()