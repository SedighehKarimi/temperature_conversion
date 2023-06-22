
import pytest
from conversion import celsius_to_fahrenheit

def test_clesius_to_fahrenheit() :
    assert celsius_to_fahrenheit(20) = 68
    assert celsius_to_fahrenheit(30) = 86
    assert celsius_to_fahrenheit(0) = 32

