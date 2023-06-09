from src import app
from unittest import TestCase
import sys
sys.path.append('../src')

class AppTest(TestCase):
   def test_lambda_handler(capsys):
    event = {'x': 3, 'y': 5}
    app.lambda_handler(event, None)
    captured = capsys.readouterr()
    assert captured.out == '8\n'

