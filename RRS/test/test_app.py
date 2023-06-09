from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class AppTest(TestCase):
    def test_home(self):
        event = {'x': 3, 'y': 5}
        result = app.lambda_handler(event, None)
        self.assertEqual(result, 8)

