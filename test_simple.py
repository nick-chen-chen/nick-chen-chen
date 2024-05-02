import pytest
import time

def test_simple():
    assert 1 == 1

def test_simple2():
    assert 1 == 1

def test_simple3():
    time.sleep(5)
    assert 1 == 1