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
        # format: https://ntsi.com/drivers-license-format/
        prefix = ['H3', '989', '7832442200652534633439'] # first part of the license
        mid = ['541', '7A28', '305'] # second part of the license
        suffix = ['112', '46', '1121'] # last part of the license
        for p in prefix: # loops through all combinations
            for m in mid:
                for s in suffix:
                    testLicense = analyze_text(f'My US Driver\'s License Number is {p}{m}{s}', ['US_DRIVER_LICENSE'])
                    if m == '7A28': # testing incorrect alphanumeric number
                        self.assertFalse(testLicense)
                    elif p == '7832442200652534633439': # testing incorrect numeric number
                        self.assertFalse(testLicense)
                    else: # Positive test case
                        self.assertTrue(testLicense, f'{p}{m}{s} is not a valid driver\'s license')
                        # [type: US_DRIVER_LICENSE, start: 33, end: 41, score: 0.4]
                        self.assertEqual(testLicense[0].entity_type, 'US_DRIVER_LICENSE')
                        if p == 'H3':
                            self.assertAlmostEqual(testLicense[0].score, 0.65, 2)
                        else:
                            self.assertAlmostEqual(testLicense[0].score, 0.4, 2)

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
