"""Unit test file for team praise_him"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_praise_him(unittest.TestCase):
    """Test team praise_him PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_es_nie(self):
        """Test ES_NIE functionality"""

    def test_es_nif(self):
        """Test ES_NIF functionality"""

    def test_fi_personal_identity_code(self):
        """Test FI_PERSONAL_IDENTITY_CODE functionality"""
        positives = [
            "My Finnish ID is 131052-308T",
            "Here is one: 010101A123A"
        ]

        for text in positives:
            result = analyze_text(text, ['FI_PERSONAL_IDENTITY_CODE'])
            self.assertTrue(result, f"Failed to detect FI PIC in: {text}")
            self.assertEqual(result[0].entity_type, 'FI_PERSONAL_IDENTITY_CODE')

        # Negative example (should NOT match)
        negative = "This text does not contain a Finnish personal identity code."
        result = analyze_text(negative, ['FI_PERSONAL_IDENTITY_CODE'])
        self.assertFalse(result)

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""

    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""
        # IP Address Format is 000.000.000.000
        prefix = ['192', '256'] # first octet
        mid1 = ['56', '100'] # second octet
        mid2 = ['76', '50'] # third octet
        suffix = ['182', '1'] # fourth octet

        # loop through all combinations of prefix, mid1, mid2, and suffix
        for p in prefix:
            for m1 in mid1:
                for m2 in mid2:
                    for s in suffix:
                        result = analyze_text(f'My IP Address is {p}.{m1}.{m2}.{s}', ['IP_ADDRESS'])

                        if p == '256':
                            # negative test-case - 200 is not valid
                            self.assertFalse(result)
                        else:
                            self.assertTrue(result, f'IP Address not recognized: {p}.{m1}.{m2}.{s}')
                            # [type: IP_ADDRESS, start: 17, end: 30, score: 0.95]
                            self.assertEqual(result[0].entity_type, 'IP_ADDRESS')
                            self.assertAlmostEqual(result[0].score, 0.95, 2)


  

if __name__ == '__main__':
    unittest.main()
