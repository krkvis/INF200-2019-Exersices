# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


def bubble_sort(data):
    """Sort list ord tuple in increasing order using the Bubble Sort algorithm.
    :param data: list or tuple with numbers in random order.
    :returns: sorted list.
    """
    data_list = list(data)
    n = len(data_list)
    while n > 0:
        i = 1
        while i < n:
            if data_list[i] < data_list[i - 1]:
                data_list[i], data_list[i - 1] = data_list[i - 1], data_list[i]
            i += 1
        n -= 1
    return data_list


def test_empty():
    """Test that the sorting function works for empty list or tuple."""
    assert bubble_sort([]) == []
    assert bubble_sort(()) == []


def test_single():
    """Test that the sorting function works for single-element list."""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """Test that the sorting function returns a new object."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data is not data


def test_original_unchanged():
    """Test that sorting leaves the original data unchanged."""
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)
    assert sorted_data == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == data


def test_sorting():
    """Test sorting for various test cases."""
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([1, 7, 3, 2, 9, 1]) == [1, 1, 2, 3, 7, 9]
    assert bubble_sort(['i', 'a', '5', 'd', '1']) == ['1', '5', 'a', 'd', 'i']
    assert bubble_sort(['good', 'day', 'sir']) == ['day', 'good', 'sir']
