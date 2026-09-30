import unittest
from converter import calculate_result
from currencies import search_currency, get_name


class TestConverter(unittest.TestCase):

    def test_calculate_result(self):
        self.assertEqual(calculate_result(100, 0.5), 50)
        self.assertEqual(calculate_result(0, 83.2), 0)

    def test_same_currency_rate(self):
        self.assertEqual(calculate_result(250, 1.0), 250)

    def test_search_by_code(self):
        self.assertIn("INR", search_currency("inr"))

    def test_search_by_name(self):
        self.assertIn("JPY", search_currency("yen"))

    def test_search_not_found(self):
        self.assertEqual(search_currency("qwerty"), [])

    def test_get_name(self):
        self.assertEqual(get_name("EUR"), "Euro")


if __name__ == "__main__":
    unittest.main()
