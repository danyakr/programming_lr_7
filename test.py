import unittest
from app import app, current_rates
from flask import json


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Тест главной страницы"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)  # Проверка, что HTML-шаблон отрендерился


    def test_get_rates_invalid_currency(self):
        """Тест для запроса с неправильным кодом валюты"""
        response = self.app.get('/get_rates?currency_code=XYZ')  # Некорректный код валюты
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid currency code')

    def test_get_rates_missing_currency_code(self):
        """Тест для запроса без кода валюты"""
        response = self.app.get('/get_rates')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Invalid currency code')



if __name__ == '__main__':
    unittest.main()
