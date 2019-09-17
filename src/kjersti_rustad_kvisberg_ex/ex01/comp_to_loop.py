# -*- coding: utf-8 -*-

__author__ = 'Kjersti Rustad Kvisberg'
__email__ = 'kjkv@nmbu.no'


def squares_by_comp(n):
    """Return a list with the squares of the numbers in range of n that gives
    a reminder of 1 when divided by three.
    :param n: Range of numbers to check.
    :return: List of squared numbers.
    """
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """Return a list with the squares of the numbers in range of n that gives
    a reminder of 1 when divided by three.
    :param n: Range of numbers to check.
    :return: List of squared numbers.
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k ** 2)
    return squares


if __name__ == '__main__':
    # Run code with arbitrary n:
    var = 5
    if squares_by_comp(var) != squares_by_loop(var):
        print('ERROR!')
