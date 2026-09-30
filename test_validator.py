import unittest
from validator import is_valid_currency, get_valid_amount, clean_code


class TestValidator(unittest.TestCase):

    def test_valid_currency(self):
        self.assertTrue(is_valid_currency("USD"))
        self.assertTrue(is_valid_currency("INR"))

    def test_invalid_currency(self):
        self.assertFalse(is_valid_currency("XYZ"))
        self.assertFalse(is_valid_currency(""))

    def test_valid_amount(self):
        self.assertEqual(get_valid_amount("100"), 100.0)
        self.assertEqual(get_valid_amount("12.5"), 12.5)
        self.assertEqual(get_valid_amount("0"), 0.0)

    def test_invalid_amount(self):
        self.assertIsNone(get_valid_amount("abc"))
        self.assertIsNone(get_valid_amount("-5"))
        self.assertIsNone(get_valid_amount(""))
        self.assertIsNone(get_valid_amount("nan"))
        self.assertIsNone(get_valid_amount("inf"))

    def test_clean_code(self):
        self.assertEqual(clean_code("  usd "), "USD")


if __name__ == "__main__":
    unittest.main()
