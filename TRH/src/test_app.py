import app
from unittest import TestCase
import sys
sys.path.append('../src')

class test(TestCase):
    def test_app(self):
        result = app.python_aws_lambda()
        self.assertEqual(result, { "suma": 4})