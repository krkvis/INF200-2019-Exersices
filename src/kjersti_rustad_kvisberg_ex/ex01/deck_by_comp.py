# -*- coding: utf-8 -*-

__author__ = 'Kjersti Rustad Kvisberg'
__email__ = 'kjkv@nmbu.no'

SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    """Create a deck of cards from lists of suits and values,
     using a for loop.
    :return: List with 52 elements, one element for each combo
        between 4 suits and 13 values.
    """
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """Create a deck of cards from lists of suits and values,
    using a list comprehension.
    :return: List with 52 elements, one element for each combo
        between 4 suits and 13 values.
    """
    return [(s, v) for s in SUITS for v in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
