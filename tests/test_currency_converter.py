import unittest
from app import app
from utils import is_valid_currency, convert_currency

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_currency_code(self):
        invalid_code = 'XYZ'
        result = is_valid_currency(invalid_code)
        self.assertFalse(result)

    def test_valid_currency_code(self):
        valid_code = 'USD'
        result = is_valid_currency(valid_code)
        self.assertTrue(result)

    def test_invalid_amount(self):
        from_currency = 'USD'
        to_currency = 'EUR'
        invalid_amount = 'abc'
        result = convert_currency(from_currency, to_currency, invalid_amount)
        self.assertIsNone(result)

    def test_valid_conversion(self):
        from_currency = 'USD'
        to_currency = 'EUR'
        amount = 100
        result = convert_currency(from_currency, to_currency, amount)
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()
