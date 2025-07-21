import pytest
from soma import soma

def test_soma():
    assert soma(2, 2) == 4
    assert soma(1, -1) == 0
    assert soma(-1, -1) == -2
    assert soma(0, 0) == 0
