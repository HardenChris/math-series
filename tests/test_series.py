#for some reason testing is broken. Yay
import pytest
from math_series.series import fibonacci
from math_series.series import lucas

def fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected



