"""Unit test file for team _x"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__x(unittest.TestCase):
    """Test team _x PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_phone_number(self):
        """Test PHONE_NUMBER functionality"""

        # Positive test cases
        valid_numbers = [
        "Call me at 123-456-7890",
        "My number is (123) 456-7890",
        "Reach me at 123 456 7890",
        "Emergency contact: +1 123-456-7890"]

        for text in valid_numbers:
            results = analyze_text(text, ["PHONE_NUMBER"])
            self.assertTrue(
                any(r.entity_type == "PHONE_NUMBER" for r in results),
                msg=f"Failed to detect PHONE_NUMBER in: {text}")

        # Negative test cases
        invalid_numbers = [
        "My code is 123-45-678",
        "Number: 123456789",
        "SSN is 123-45-6789",
        "Random number 987654"]
            
        for text in invalid_numbers:
            results = analyze_text(text, ["PHONE_NUMBER"])
            self.assertEqual(len(results),0,msg=f"Incorrectly detected PHONE_NUMBER in: {text}")


    def test_location(self):
        """Test LOCATION functionality"""
        #Positive tests
        #City
        results = analyze_text("John lives in Houston", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0)
        #Country
        results = analyze_text("Maria is visiting Canada", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0)
        #State
        results = analyze_text("They moved to California", ["LOCATION"])
        print(results)
        self.assertTrue(len(results) > 0) 

        #Negative test
        results = analyze_text("Billy likes pizza", ["LOCATION"])
        print(results)
        self.assertEqual(len(results), 0)

    def test_person(self):
        """Test PERSON functionality"""
        results = analyze_text("Alice and Bob went to school", ["PERSON"])
        self.assertTrue(
            all(r.entity_type == "PERSON" for r in results),
            msg="Failed to detect PERSON entity"

        )

        results = analyze_text("There are no names here", ["PERSON"])
        self.assertEqual(
            len(results), 0,
            msg="Incorrectly detected PERSON entity"
        )
    

    def test_uk_nhs(self):
        """Test UK_NHS functionality"""
        # Positive test cases
        text_with_nhs = "Patient NHS number is 943 476 5919"
        results = analyze_text(text_with_nhs, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertGreater(len(nhs_results), 0, "Should detect NHS number with spaces")
    
        text_no_spaces = "NHS number: 9434765919"
        results = analyze_text(text_no_spaces, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertGreater(len(nhs_results), 0, "Should detect NHS number without spaces")
    
        # Negative test case
        text_invalid = "Patient ID: 123 456 789"  # Only 9 digits
        results = analyze_text(text_invalid, ["UK_NHS"])
        nhs_results = [r for r in results if r.entity_type == "UK_NHS"]
        self.assertEqual(len(nhs_results), 0, "Should not detect invalid NHS number")

    def test_uk_nino(self):
        """Test UK_NINO functionality"""


if __name__ == '__main__':
    unittest.main()
