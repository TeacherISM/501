# test_hello_world.py
import pytest
from src import app

def test_lambda_handler():
    response = app.handler(None, None)
    assert response == "Hello, world! A01352283"