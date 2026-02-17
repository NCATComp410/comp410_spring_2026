"""Unit test file for team _3"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__3(unittest.TestCase):
    """Test team _3 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_url(self): # By Makell M Williams, with help from the video and Google Gemini.
        """Test URL functionality"""
        # Followed the video to hide the url parts in lists.
        start = ['www', 'http', 'https'] # Typical beginning of a url.
        middle = ['game', 'plane'] # Some basic domains, may or may not actually exists.
        end = ['com', 'edu', '000'] # 2 normal top level domains and a fake one '000'

        # Loop to begin testing all combos of the info above.
        # These are all positive test cases since the URL recognizer does not attempt
        # to discard invalid urls.  See the source here
        # https://github.com/microsoft/presidio/blob/4a2672d64b3a8883f3328b367b13d3f5a3242465/presidio-analyzer/presidio_analyzer/predefined_recognizers/generic/url_recognizer.py#L6
        for s in start:
            for m in middle:
                for e in end:
                    result = analyze_text(f"My url {s}.{m}.{e}", ['URL']) # My URL being analyzed.
                    self.assertEqual(result[0].entity_type, "URL")

        # Negative test cases without a url
        result = analyze_text("My url http//nothing/at/all", ['URL'])
        self.assertFalse(result)

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""
        # format: 9 digits, can contain dashes
        # begins with 9
        # 4th and 5th digit ranges: (50-65), (70-88), (90-92, (94-99)
        prefix = ['923', '989', '789'] # first part of the ITIN
        mid = ['541', '728', '305'] # second part of the ITIN
        suffix = ['112', '46', '1121'] # last part of the ITIN
        for p in prefix: # loops through all combinations
            for m in mid:
                for s in suffix:
                    testITIN = analyze_text(f'My US Bank Number is {p}{m}{s}', ['US_ITIN'])
                    if p == '789': # testing SSN number
                        self.assertFalse(testITIN)
                    elif s == '46': # testing number too short
                        self.assertFalse(testITIN)
                    elif s == '1121': # testing number too long
                        self.assertFalse(testITIN)
                    elif m == '305': # testing 4th and 5th digit outside of bounds
                        self.assertFalse(testITIN)
                    else: # Positive test case
                        self.assertTrue(testITIN, f'{p}{m}{s} is not a valid passport')
                        # [type: US_ITIN, start: 21, end: 30, score: 0.3]
                        self.assertEqual(testITIN[0].entity_type, 'US_ITIN')
                        self.assertAlmostEqual(testITIN[0].start, 21, 2)
                        self.assertAlmostEqual(testITIN[0].end, 30, 2)
                        self.assertAlmostEqual(testITIN[0].score, 0.3, 2)


    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
