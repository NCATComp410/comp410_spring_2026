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
        entity_list = ["US_BANK_NUMBER"]

        # Positive
        text1 = "Routing number: 021000021"
        r1 = analyze_text(text1, entity_list)
        self.assertTrue(any(r.entity_type == "US_BANK_NUMBER" for r in r1),
                        f"Failed to detect valid routing number in: {text1}")

        # Positive
        text2 = "My bank routing number is 011000015."
        r2 = analyze_text(text2, entity_list)
        self.assertTrue(any(r.entity_type == "US_BANK_NUMBER" for r in r2),
                        f"Failed to detect valid routing number in: {text2}")

        # Negative 
        text3 = "Routing number: 0210/00021"
        r3 = analyze_text(text3, entity_list)
        self.assertFalse(any(r.entity_type == "US_BANK_NUMBER" for r in r3),
                 f"False positive detected in: {text3}")


           
        

    def test_us_driver_license(self):
        """Test US_DRIVER_LICENSE functionality"""

    def test_us_itin(self):
        """Test US_ITIN functionality"""

    def test_us_passport(self):
        """Test US_PASSPORT functionality"""


if __name__ == '__main__':
    unittest.main()
