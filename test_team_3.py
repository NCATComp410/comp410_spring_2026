"""Unit test file for team _3"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__3(unittest.TestCase):
    """Test team _3 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self):
        """Test URL functionality"""

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""
        # format: letter or number + 8 numbers
        prefix = ['A12','B98', '%90', '038'] # first part of the passport
        mid = ['345','765', 'C21'] # second part of the passport
        suffix = ['678','432'] # last part of the passport
        for p in prefix: # loops through all combinations
            for m in mid:
                for s in suffix:
                    testPassport = analyze_text(f'My US Passport is {p}{m}{s}', ['US_PASSPORT'])
                    if m == 'C21': # testing non numerical value besides first value
                        self.assertFalse(testPassport)
                    elif p == '%90': # testing passport containing non-alphanumerical value
                        self.assertFalse(testPassport)
                    else: # Positive test case
                        self.assertTrue(testPassport, f'{p}{m}{s} is not a valid passport')
                        # [type: US_PASSPORT, start: 18, end: 27, score: 0.44999999999999996]
                        self.assertEqual(testPassport[0].entity_type, 'US_PASSPORT')
                        self.assertAlmostEqual(testPassport[0].start, 18, 2)
                        self.assertAlmostEqual(testPassport[0].end, 27, 2)
                        if p == '038': # testing older passport(full numerical)
                            self.assertAlmostEqual(testPassport[0].score, 0.4, 2)
                        else:
                            self.assertAlmostEqual(testPassport[0].score, 0.45, 2)
        


if __name__ == '__main__':
    unittest.main()
