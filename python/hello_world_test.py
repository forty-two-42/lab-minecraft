import pytest
from hello_world import sum_two_integers

def test_sum_two_integers():
    assert (1+1) == 2

    a=11
    b=22
    
    c = sum_two_integers(a, b)

    assert c == 33

