import pytest
from src import app

def test_lambda_handler():
    response = app.handler(None, None)
    assert response == {
        "suma": 3,
    }
    