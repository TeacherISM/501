import pytest
import ggp.python3.lambda_func as lambda_func


def test_addNums():

    assert lambda_func.addNums() == 2
