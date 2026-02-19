"""Unit test file for team praise_him"""
import unittest
import string
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

    def test_iban_code(self):
        """Test IBAN_CODE functionality"""
        # dictionary with letters and their ASCII conversions
        ascii_to_letters = {
            ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)
        }

        # sample country codes and length
        country_codes = {
            'AD': 6, 
            'AL': 7, 
            'AT': 5, 
            'EE': 5,
            'XY': 9        # negative case
        }

        # generate fake bank number
        # the value of num groups defines how many groups of 4 alphanumeric numbers (or 0000 in this case) we want in our IBAN code
        # Each number of groups is different for each country codes
        def test_make_fake_number(num_groups):
            groups = ""
            for i in range(num_groups):
                # just generate a bank number full of zeros for simplicity
                groups += "0000"

                # # generate random numbers in groups of 4
                # for j in range(4):
                #     groups += str(random.randint(0, 9))
        
            return groups

        # turn iban into number
        def test_to_number_iban(p_iban):
            t_iban = (p_iban[:2] + "00" + p_iban[4:]).upper()
            return (t_iban[4:] + t_iban[:4]).translate(ascii_to_letters)
        
        # create check digit from number iban using the MOD97 algorithm
        def test_make_check_digit(n_iban):
            return f"{98 - (int(n_iban) % 97):0>2}"
        
        # run cases for each combination of country code and check digit
        text = ""
        for code, num_groups in country_codes.items():
            iban = code + "00" + test_make_fake_number(num_groups)

            # create list of check digits. algorithm shouldn't generate 00.
            check_digits = [
                "00",                                       # negative case
                test_make_check_digit(test_to_number_iban(iban))      # positive case
            ]

            for digit in check_digits:
                new_iban = iban[:2] + digit + iban[4:]
                text = f"My IBAN code is {new_iban}"
                result = analyze_text(text, ['IBAN_CODE'])

                # no number of groups should be greater than 8
                if num_groups > 8:
                    #print("\ngreater than 8")
                    self.assertFalse(result)
                
                # checksum is most likely not going to be 00
                elif digit == "00":
                    #print("\nchecksum is 00")
                    self.assertFalse(result)

                # valid
                else:
                    self.assertTrue(result, f"IBAN code: {new_iban}, not recognized.")
                    print(f"\n validating {new_iban}")
                    self.assertEqual(result[0].entity_type, 'IBAN_CODE')
                    self.assertAlmostEqual(result[0].score, 1.0, 2)



    def test_ip_address(self):
        """Test IP_ADDRESS functionality"""


if __name__ == '__main__':
    unittest.main()
