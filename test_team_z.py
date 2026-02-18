"""Unit test file for team _z"""
import unittest
from pii_scan import analyze_text, show_aggie_pride  # noqa 


class TestTeam__z(unittest.TestCase):
    """Test team _z PII functions"""
    def test_show_aggie_pride(self):
        """Test to make sure Aggie Pride is shown correctly"""
        self.assertEqual(show_aggie_pride(), "Aggie Pride - Worldwide")

    def test_th_tnin(self):
        """Test TH_TNIN functionality"""

    def test_kr_rrn(self):
        """Test KR_RRN functionality"""

        # Positive case
        text_positive = "내 주민등록번호는 900101-1234567 입니다."
        results_positive = analyze_text(text_positive, ["KR_RRN"])
        self.assertTrue(any(r.entity_type == "KR_RRN" for r in results_positive))

        # Negative case
        text_negative = "잘못된 번호: 900101-123456"
        results_negative = analyze_text(text_negative, ["KR_RRN"])
        self.assertFalse(any(r.entity_type == "KR_RRN" for r in results_negative))


    def test_in_gstin(self):
        """Test IN_GSTIN functionality"""

    def test_sg_nric_fin(self):
        """Test SG_NRIC_FIN functionality"""

    def test_sg_uen(self):
        """Test SG_UEN functionality"""


if __name__ == '__main__':
    unittest.main()
