from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class AppTest(TestCase):
    def test_home(self):
        result = app.handler(4, 5)
        self.assertEqual(result, 9)

