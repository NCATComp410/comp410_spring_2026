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
        p1, p2, p3, p4 = "4111", "1111", "1111", "1111"
        positive_text = f"My credit card number is {p1} {p2} {p3} {p4}."

        # Analyze the text and check if the CREDIT_CARD entity is detected
        pos_result = analyze_text(text=positive_text, entity_list=["CREDIT_CARD"])
        self.assertTrue(pos_result, f"Expected to find a CREDIT_CARD entity in the text: {positive_text}")

        # Check if the detected entity is of type CREDIT_CARD
        self.assertEqual(pos_result[0].entity_type, "CREDIT_CARD")

        # Check if the detected value matches the expected credit card number
        matched_value = positive_text[pos_result[0].start:pos_result[0].end]
        cleaned_value = matched_value.replace(" ", "").replace("-", "") 

        # Check if the cleaned value consists of only digits and has a valid length for credit card numbers
        self.assertTrue(cleaned_value.isdigit()) # Ensure the cleaned value contains only digits
        self.assertGreaterEqual(len(cleaned_value), 13, f"Expected a valid credit card number with at least 13 digits, got: {cleaned_value}")
        self.assertLessEqual(len(cleaned_value), 19, f"Expected a valid credit card number with at most 19 digits, got: {cleaned_value}")

        # Check if the confidence score is above a reasonable threshold
        self.assertGreaterEqual(pos_result[0].score,0.3)

        # Negative test case
        n1, n2, n3, n4 = "4111", "1111", "1111", "1112"  # Invalid credit card number
        negative_text = f"My credit card number is {n1} {n2} {n3} {n4}."

        # Analyze the negative text and ensure no CREDIT_CARD entity is detected
        neg_result = analyze_text(text=negative_text, entity_list=["CREDIT_CARD"])
        self.assertFalse(neg_result, f"Expected no CREDIT_CARD entity in the text: {negative_text}")




    def test_crypto(self):
        """Test CRYPTO functionality"""

    def test_date_time(self):
        """Test DATE_TIME functionality"""

    def test_email_address(self):
        """Test EMAIL_ADDRESS functionality"""

    def test_medical_license(self):
        """Test MEDICAL_LICENSE functionality"""


if __name__ == '__main__':
    unittest.main()
