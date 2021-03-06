# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import pytest


def median(data):
    """Returns median of data.
    Source: "https://bit.ly/2n5qLs4"

    :param data: An iterable containing numbers
    :return: Median of data
    """
    s_data = sorted(data)
    n = len(s_data)
    if n == 0:
        raise ValueError
    else:
        return (s_data[n//2] if n % 2 == 1
                else 0.5 * (s_data[n//2 - 1] + s_data[n//2]))


def test_single():
    """Tests that the median function returns the correct value for a single
    element list.
    """
    assert median([1]) == 1


def test_odd_numbered():
    """Tests that the median function returns the correct value for odd
    numbered list.
    """
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3


def test_even_numbered():
    """Tests that the median function returns the correct value for even
    numbered list.
    """
    data = [1, 2, 3, 4]
    assert median(data) == 2.5


def test_differently_ordered():
    """Tests that the median function returns the correct value for ordered,
    reverse-ordered and unordered lists.
    """
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([5, 4, 3, 2, 1]) == 3
    assert median([5, 2, 3, 1, 4]) == 3


def test_empty():
    """Tests that the median function raises a ValueError for empty lists."""
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    """Tests that the median function leaves the original data unchanged."""
    data = [1, 2, 3]
    median(data)
    assert data == [1, 2, 3]


def test_tuples():
    """Tests that the median function works for tuples."""
    assert median((1, 2, 3)) == 2
