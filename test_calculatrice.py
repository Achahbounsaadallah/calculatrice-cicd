import pytest
from calculatrice import addition, soustraction, multiplication, division
def test_addition():
	assert addition(2, 3) == 5