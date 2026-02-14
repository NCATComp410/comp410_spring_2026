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

    def test_it_identity_card(self):
        """Test IT_IDENTITY_CARD functionality"""

    def test_it_passport(self):
        """Test IT_PASSPORT functionality"""

    def test_it_vat_code(self):
        """Test IT_VAT_CODE functionality"""


if __name__ == '__main__':
    unittest.main()
