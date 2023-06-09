import pytest
from python import lambda_func

# Test coverage
def test_add():
    assert lambda_func.add() == 2
