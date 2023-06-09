import pytest
import ggp.lambda_func as lambda_func

# Test coverage
def test_addNums():
    assert lambda_func.addNums() == 2
