import pytest
from unittest import TestCase
import sys
sys.path.append('../src')
from src import app

class test(TestCase):
    def test_app(self):
        result = app.python_aws_lambda()
        self.assertEqual(result, { "suma": 4})