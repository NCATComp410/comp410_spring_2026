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
