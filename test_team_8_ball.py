"""Unit test file for team 8_ball"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam_8_ball(unittest.TestCase):
    """Test team 8_ball PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_aba_routing_number(self):
        """Test ABA_ROUTING_NUMBER functionality"""
        #ABA Routing number format 
        prefix = ["0110", "0210"] # first 4 numbers 
        mid = ["0001", "0000"] # middle of the numbers 
        suffix = ["5", "1"] #end of the numbers 

        #loop through all combinations
        for p,m,s in zip(prefix,mid,suffix):
            result = analyze_text(f"My ABA Routing Number is {p}-{m}-{s}",['ABA_ROUTING_NUMBER'])
            if m == '0000':
                #negative testcase - 0000 is not valid 
                self.assertFalse(result)
            else: 
                #positive testcase 

                self.assertTrue(result, f'ABA not recongized {p}{m}{s}')
                #[type: ABA_ROUTING_NUMBER, start: 25, end: 34, score: 1.0]\
                self.assertEqual(result[0].entity_type, 'ABA_ROUTING_NUMBER')
                self.assertAlmostEqual(result[0].score, 1.0, 2)

    def test_au_abn(self):
        """Test AU_ABN functionality"""

    def test_au_acn(self):
        """Test AU_ACN functionality"""
        # ------------------------
        # POSITIVE TEST CASES
        # ------------------------

        # Valid ACN – continuous format
        valid_continuous = ["004085616"]
        for acn in valid_continuous:
            result = analyze_text(f"My ACN is {acn}", ['AU_ACN'])
            self.assertTrue(result)
            self.assertEqual(result[0].entity_type, 'AU_ACN')

        # Valid ACN – spaced format
        valid_spaced = ["004 085 616"]
        for acn in valid_spaced:
            result = analyze_text(
                f"Australian Company Number {acn}",
                ['AU_ACN']
            )
            self.assertTrue(result)
            self.assertEqual(result[0].entity_type, 'AU_ACN')

        # Valid ACN – hyphen format
        valid_hyphen = ["004-085-616"]
        for acn in valid_hyphen:
            result = analyze_text(f"ACN: {acn}", ['AU_ACN'])
            self.assertTrue(result)
            self.assertEqual(result[0].entity_type, 'AU_ACN')

        # ------------------------
        # NEGATIVE TEST CASES
        # ------------------------

        # Wrong length (too short)
        short_numbers = ["12345678"]
        for num in short_numbers:
            result = analyze_text(f"ACN {num}", ['AU_ACN'])
            self.assertFalse(result)

        # Wrong length (too long)
        long_numbers = ["1234567890"]
        for num in long_numbers:
            result = analyze_text(f"ACN {num}", ['AU_ACN'])
            self.assertFalse(result)

        # Contains letters
        invalid_letters = ["12345A789"]
        for num in invalid_letters:
            result = analyze_text(f"ACN {num}", ['AU_ACN'])
            self.assertFalse(result)

        # No ACN context (just 9 digits)
        result = analyze_text("Order number 123456789", ['AU_ACN'])
        self.assertFalse(result)

        # Invalid checksum (wrong last digit)
        result = analyze_text("ACN 004085617", ['AU_ACN'])
        self.assertFalse(result)

    def test_au_medicare(self):
        """Test AU_MEDICARE functionality"""

    def test_au_tfn(self):
        """Test AU_TFN functionality"""
        # positive examples
        valid = ["123456782", "123 456 782", "000000000"]
        for tfn in valid:
            result = analyze_text(f"My TFN is {tfn}", ['AU_TFN'])
            self.assertTrue(result)
            self.assertEqual(result[0].entity_type, 'AU_TFN')

        # negative examples (wrong length)
        invalid = ["12345678", "1234567890"]
        for bad in invalid:
            result = analyze_text(f"My TFN is {bad}", ['AU_TFN'])
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
