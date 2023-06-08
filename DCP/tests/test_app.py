from src import app
import pytest
import sys
sys.path.append('../src')


def test_lambda_handler():
    result = app.lambda_handler(None , None)
    assert result == "Hola, A01781631"
