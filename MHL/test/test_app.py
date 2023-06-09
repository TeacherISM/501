# test_hello_world.py
from MHL.src import app

def test_lambda_handler():
    response = app.handler(None, None)
    assert response == {
        "suma": 3,
    }
    
