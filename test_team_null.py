"""Unit test file for team null"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa


class TestTeam_null(unittest.TestCase):
    """Test team null PII functions"""

    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_us_ssn(self):
        """Test US_SSN functionality"""
        # SSN format is 000-00-0000
        prefix = ['123', '321']  # first part of the SSN
        mid = ['12', '00']  # middle of the SSN
        suffix = ['1234', '4321']  # end of the SSN
        # loop through all combinations of prefix, mid, and suffix
        for p in prefix:  # this is the prefix
            for m in mid:  # this is the middle
                for s in suffix:  # this is the suffix
                    result = analyze_text(f'My SSN is {p}-{m}-{s}', ['US_SSN'])
                    if m == '00':
                        # negative testcase - 00 is not valid
                        self.assertFalse(result)
                    else:
                        # positive testcase
                        self.assertTrue(result, f'SSN not recognized {p}-{m}-{s}')
                        #[type: US_SSN, start: 10, end: 21, score: 0.85]
                        self.assertEqual(result[0].entity_type, 'US_SSN')
                        self.assertAlmostEqual(result[0].score, 0.85, 2)


if __name__ == '__main__':
    unittest.main()
