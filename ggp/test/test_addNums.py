import pytest
from lambda_f import lambda_func

# Test coverage
def test_addNums():
    assert lambda_func.addNums() == 2
