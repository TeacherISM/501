import pytest
from addFunc import lambda_func

# Test coverage
def test_addNums():
    assert lambda_func.addNums() == 2
