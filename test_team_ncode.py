"""Unit test file for team ncode"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_ncode(unittest.TestCase):
    """Test team ncode PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_credit_card(self):
        """Test CREDIT_CARD functionality"""

    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""
        # Positive test cases - valid dates and times that should be detected
        valid_datetime = [
            # Date formats
            '12/01/1990',
            '01/15/2023',
            '1/1/2000',
            '06/30/1985',
            '3/5/2024',
            'January 1, 2023',
            '2023-01-15',
            'March 15th, 2020',
            # Time formats with context
            '3:30 PM',
            '9:00 AM',
            '2:45 PM',
            # Date and time combined
            '12/01/1990 at 3:30 PM',
            'January 15, 2023 at 2:45 PM',
            '2023-01-15 14:30',
            'March 5th, 2024 9:00 AM',
            # Relative times
            'tomorrow',
            'yesterday',
            'next week',
            'last month',
            'next Friday',
            'last year'
        ]
        
        for datetime_str in valid_datetime:
            result = analyze_text(f'The meeting is scheduled for {datetime_str}', ['DATE_TIME'])
            self.assertTrue(result, f'DATE_TIME not recognized: {datetime_str}')
            self.assertEqual(result[0].entity_type, 'DATE_TIME', 
                           f'Wrong entity type for: {datetime_str}')
            # Score should be reasonably high
            self.assertGreater(result[0].score, 0.5, 
                             f'Score too low ({result[0].score}) for {datetime_str}')
        
        # Negative test cases - text that should NOT be detected as DATE_TIME
        invalid_datetime = [
            'random text here',
            'hello world',
            'not a date at all',
            'just some numbers like one two three',
            'the price is expensive',
            'my favorite color is blue',
            'artificial intelligence',
            'Python programming language',
            'this sentence has no temporal information'
        ]
        
        for text in invalid_datetime:
            result = analyze_text(f'This is some text: {text}', ['DATE_TIME'])
            # Should either return empty list or not detect DATE_TIME
            if result:
                # If something was detected, it shouldn't be DATE_TIME
                has_datetime = any(r.entity_type == 'DATE_TIME' for r in result)
                self.assertFalse(has_datetime, 
                               f'DATE_TIME incorrectly detected in: {text}')

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
