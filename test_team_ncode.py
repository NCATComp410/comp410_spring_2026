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

        # Positive test case

        # Different test cards
        positives = [
            ("4111", "1111", "1111", "1111"),  # Visa
            ("5555", "5555", "5555", "4444"),  # Mastercard
            ("3782", "822463", "10005", ""),   # AmEx
            ("6011", "1111", "1111", "1117"),  # Discover
        ]

        # Go through each test card
        for parts in positives:
            # Remove empty strings
            chunks = [p for p in parts if p]
            positive_text = f"My credit card number is {' '.join(chunks)}."

            # Analyze the text and check if the CREDIT_CARD entity is detected
            pos_result = analyze_text(
                text=positive_text, entity_list=["CREDIT_CARD"])
            self.assertTrue(
                pos_result, f"Expected to find a CREDIT_CARD entity in the text: {positive_text}")

            # Check if the detected entity is of type CREDIT_CARD
            self.assertEqual(pos_result[0].entity_type, "CREDIT_CARD")

            # Check if the detected value matches the expected credit card number
            matched_value = positive_text[pos_result[0].start:pos_result[0].end]
            cleaned_value = matched_value.replace(" ", "").replace("-", "")

            # Check if the cleaned value consists of only digits and has a valid length for credit card numbers
            # Ensure the cleaned value contains only digits
            self.assertTrue(cleaned_value.isdigit())
            self.assertGreaterEqual(len(
                cleaned_value), 13, f"Expected a valid credit card number with at least 13 digits, got: {cleaned_value}")
            self.assertLessEqual(len(
                cleaned_value), 19, f"Expected a valid credit card number with at most 19 digits, got: {cleaned_value}")

            # Check if the confidence score is above a reasonable threshold
            self.assertGreaterEqual(pos_result[0].score, 0.3)

        # Negative test case
        negatives = [
            ("4111", "1111", "1111", "1112"),   # wrong/invalid numbers
            ("9111", "1111", "1111", "1111"), # unsupported numbers
            ("4111", "1111", "1111", "11"), # short numbers
        ]

        for parts in negatives:
            negative_text = f"My credit card number is {' '.join(parts)}."

            # Analyze the negative text and ensure no CREDIT_CARD entity is detected
            neg_result = analyze_text(
                text=negative_text, entity_list=["CREDIT_CARD"])
            self.assertFalse(
                neg_result, f"Expected no CREDIT_CARD entity in the text: {negative_text}")

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
        #Positive test
        valid_email = "john.doe@example.com"
        result = analyze_text(f"My email is {valid_email}", entity_list=['EMAIL_ADDRESS'])
        self.assertTrue(result, f"Email is not recognized {valid_email}")
        self.assertEqual(result[0].entity_type, 'EMAIL_ADDRESS')

        #Negative test    
        invalid_email = "Bob.smith@@localhost"
        result = analyze_text(f"My email is {invalid_email}", entity_list=['EMAIL_ADDRESS'])
        self.assertFalse(result, 'EMAIL_ADDRESS')

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
