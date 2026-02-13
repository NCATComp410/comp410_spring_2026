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
        for s in start:
            for m in middle:
                for e in end:

                    result = analyze_text(f"My url {s}.{m}.{e}", ['URL']) # My URL being analyzed.
                    
                    # Got a little bit of help from Google Gemini, since I didn't understand the result would return what should be an empty list.
                    if e == '000': # My negative test cases, since '000' is an invalid top level domain.
                        print(f"URL {s}.{m}.{e} is not valid!")
                        self.assertEqual(len(result), 1)

                    else: # My positive test cases, since everything else should be fine.
                        print(f"URL {s}.{m}.{e} is valid!")
                        self.assertTrue(result, f"URL {s}.{m}.{e}")

    def test_us_bank_number(self):
        """Test US_BANK_NUMBER functionality"""

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
