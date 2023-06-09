import sys
import os 
from src import app
from unittest import TestCase
sys.path.append('../src')


class AppTest(TestCase):
    def test_handler(self):
        result = app.lambda_handler(None, None)
        assert result['statusCode'] == 200
        assert result['body'] == 18


