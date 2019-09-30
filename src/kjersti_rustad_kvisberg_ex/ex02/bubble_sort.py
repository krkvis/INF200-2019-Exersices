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


if __name__ == "__main__":
    for element in ((),
                    (1,),
                    (1, 3, 8, 12),
                    (12, 8, 3, 1),
                    (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(element, bubble_sort(element)))
