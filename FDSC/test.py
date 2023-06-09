import pytest
from app import number_sum


def test_simplesum():
	assert number_sum(1,2) == 3

def test_badsum():
	assert number_sum("1",2)==None

def test_floatsum():
	assert number_sum(1.5,1.5)==None

if __name__ == '__main__':
    pytest.main()