"""Unit test file for team _1"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__1(unittest.TestCase):
    """Test team _1 PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_in_aadhaar(self):
        """Test IN_AADHAAR functionality"""

        valids = ['234567890124', '345678901238', '456789012341']
        invalids = ['123456789012', '12d3984D03', '234567843429012', '123456654321'] # Invalid codes if you want to try them

        for a in valids:
            result = analyze_text(f"My Uidai number is {a}", ['IN_AADHAAR'])

            if a[0] == '1' or a[0] == '0':
                # Negative case (invalid starting number)
                self.assertFalse(result, "AADHAAR should not start with 0 or 1")

            else:
                # Positive cases
                self.assertTrue(result, "AADHAAR number not being picked up, check the regex pattern or context words "
                "(likely a verhoeff checksum issue if you picked the number yourself)")
                self.assertEqual(result[0].entity_type, 'IN_AADHAAR')
                
                # We can set the approximation test to 1.0 since the context boosters are particular (UIDAI and AADHAAR)
                # [type: IN_AADHAAR, start: 19, end: 31, score: 1.0]
                self.assertAlmostEqual(result[0].score, 1.0, 2)




    def test_in_pan(self):
        """Test IN_PAN functionality"""
        entity_list = ["IN_PAN"]

        # positive test case 1
        text1 = "My PAN is ABCDE1234F."
        results1 = analyze_text(text1, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results1), results1)

        # positive test case 2
        text2 = "Permanent Account Number: PQRST6789L"
        results2 = analyze_text(text2, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results2), results2)

        # positive test case 3
        text3 = "pan number is abcdp1234k"
        results3 = analyze_text(text3, entity_list)
        self.assertTrue(any(r.entity_type == "IN_PAN" for r in results3), results3)

        # negative case- Incorrect format
        text4 = "PAN: ABCD1234F"
        results4 = analyze_text(text4, entity_list)
        self.assertFalse(any(r.entity_type == "IN_PAN" for r in results4), results4)

        # negative case- invalid structure
        text5 = "PAN: ABCDEFGHIJ"
        results5 = analyze_text(text5, entity_list)
        self.assertFalse(any(r.entity_type == "IN_PAN" for r in results5), results5)
    

    def test_in_passport(self):
        """Test IN_PASSPORT functionality"""

        entity_list = ["IN_PASSPORT"]

        # Positive case 1
        text1 = "My passport number is A1234567."
        results1 = analyze_text(text1, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results1), results1

        # Positive case 2
        text2 = "Indian Passport No: Z7654321 for travel."
        results2 = analyze_text(text2, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results2), results2

        # Positive case 3
        text3 = "Passport No. B1234567 is listed on the form."
        results3 = analyze_text(text3, entity_list)
        assert any(r.entity_type == "IN_PASSPORT" for r in results3), results3

        # Negative case (same format but no passport context)
        text4 = "Reference code AB1234567 was used for shipment."
        results4 = analyze_text(text4, entity_list)
        assert not any(r.entity_type == "IN_PASSPORT" for r in results4), results4

    def test_in_vehicle_registration(self):
        """Test IN_VEHICLE_REGISTRATION functionality"""
        entity_list = ["IN_VEHICLE_REGISTRATION"]

        # Positive case 1: Standard Delhi Private Vehicle (DL = Delhi)
        text1 = "The car registration number is DL10CJ1234."
        results1 = analyze_text(text1, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results1), 
                        f"Failed to detect valid Delhi plate in: {text1}")

        # Positive case 2: Maharashtra Commercial Plate (MH = Maharashtra)
        text2 = "Please log the vehicle plate MH12AB5678 for the permit."
        results2 = analyze_text(text2, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results2), 
                        f"Failed to detect valid Maharashtra plate in: {text2}")

        # Positive case 3: Karnataka registration (KA = Karnataka)
        text3 = "The suspect was driving a vehicle with registration KA01MG9999."
        results3 = analyze_text(text3, entity_list)
        self.assertTrue(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results3), 
                        f"Failed to detect valid Karnataka plate in: {text3}")

        # Negative case
        # 'ZZ' is not a valid Indian State Code, so the pattern match should fail.
        text4 = "Internal warehouse bin location is ZZ99XX0000."
        results4 = analyze_text(text4, entity_list)
        self.assertFalse(any(r.entity_type == "IN_VEHICLE_REGISTRATION" for r in results4), 
                         f"False positive detected for invalid state code in: {text4}")
        
    def test_in_voter(self):
        """Test IN_VOTER functionality"""
        # first 3 characters of IN_VOTER
        prefix = ["AAA", "GHJ", "333", "3A4"] # first part of IN_VOTER
        # last 7 digits of IN_VOTER
        suffix = ["1234567", "2348764", "5703067","4570274"] # second part of IN_VOTER

        # iterate through the prefix and suffix test cases
        for p in prefix:
            for s in suffix:

                result = analyze_text(f"My IN_Voter is {p}{s}", ['IN_VOTER'])
                
                # negative test case, first 3 characters need to be alphabetical
                if not p.isalpha():
                    self.assertFalse(result)
                else:
                     # positive test cases
                    self.assertTrue(result,f"IN_VOTER not recognized{p}{s}")
                    self.assertEqual(result[0].entity_type, "IN_VOTER")
                    self.assertAlmostEqual(result[0].score, 0.75,2)


if __name__ == '__main__':
    unittest.main()
