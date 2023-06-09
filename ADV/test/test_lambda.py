import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import AWS_Lambda as handler

def test_handler():
    ret = handler(None, None)
    assert ret['statusCode'] == 200
    assert ret['body'] == 3