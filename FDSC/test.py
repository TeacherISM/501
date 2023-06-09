import pytest
from app import lambda_handler


def test_simplesum():

	assert lambda_handler({"number_one":1, "number_two":2},{}) == 3

def test_badsum():
	assert lambda_handler({"number_one":"1", "number_two":2},{})==None

def test_floatsum():
	assert lambda_handler({"number_one":1.5, "number_two":1.5},{})==None

if __name__ == '__main__':
    pytest.main()