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
        # format: 8-17 numbers
        prefix = ['123', '453456', '76456463435433589'] # first part of the number
        mid = ['34', '765435', 'C21'] # second part of the number
        suffix = ['678', '43632', '1'] # last part of the number
        for p in prefix: # loops through all combinations
            for m in mid:
                for s in suffix:
                    testBankNumber = analyze_text(
                        f'My US Bank Number is {p}{m}{s}', ['US_BANK_NUMBER'])
                    if p == '76456463435433589': # testing length too large
                        self.assertFalse(testBankNumber)
                    elif m == 'C21': # testing number contains alphabetical value
                        self.assertFalse(testBankNumber)
                    elif p == '123' and m == '34' and s == '1': # testing length too small
                        self.assertFalse(testBankNumber)
                    else: # Positive test case
                        print(testBankNumber)
                        self.assertTrue(testBankNumber, f'{p}{m}{s} is not a valid bank number')
                        # [type: US_BANK_NUMBER, start: 21, end: 31, score: 0.4]
                        self.assertEqual(testBankNumber[0].entity_type, 'US_BANK_NUMBER')
                        self.assertAlmostEqual(testBankNumber[0].score, 0.4, 2)

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
