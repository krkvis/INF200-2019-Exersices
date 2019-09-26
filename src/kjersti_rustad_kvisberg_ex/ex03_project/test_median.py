# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


def median(data):
    """Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single():
    """Tests that the median function returns the correct value for a single
    element list.
    """
    assert median([1]) == 1


def test_odd_numbered():
    """Tests that the median function returns the correct value for odd
    numbered list.
    """
    data = [3, 2, 1]
    assert median(data) == 2


def test_even_numbered():
    """Tests that the median function returns the correct value for even
    numbered list.
    """
    data = [2, 4, 1, 3]
    assert median(data) == 2.5


def test_different_orders():
    """

    """
    pass


def test_empty():
    """

    """
    pass


def test_original_unchanged():
    """

    """
    pass


def test_tuples():
    """

    """
    pass
