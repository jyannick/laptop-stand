import pytest

from utils import add, flip_horizontally, flip_vertically


def test_add():
    assert add((1, 2), (3, 4)) == (4, 6)
    assert add((1, 2), (3, 4), (5, 6)) == (9, 12)
    assert add((1, 2), (3, 4), (5, 6), (-5, -10)) == (4, 2)
    with pytest.raises(AssertionError):
        add((1, 2), (1, 2, 3))
    with pytest.raises(AssertionError):
        add((1,), (1, 2))


def test_flip_horizontally():
    assert flip_horizontally((2, 3)) == (-2, 3)
    assert flip_horizontally((-2, -3)) == (2, -3)


def test_flip_vertically():
    assert flip_vertically((2, 3)) == (2, -3)
    assert flip_vertically((-2, -3)) == (-2, 3)
