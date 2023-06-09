from src import app
from unittest import TestCase
import sys
sys.path.append('../src')


class AppTest(TestCase):
    def test_handler(self):
        result = app.lambda_handler(None , None)
        self.assertEqual(result, 4)
