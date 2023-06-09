import sys
from src import app
from unittest import TestCase

sys.path.append('../src')

class AppTest(TestCase):
    def test_app(self):
        result = app.lambda_handler()
        self.assertEqual(result, suma)