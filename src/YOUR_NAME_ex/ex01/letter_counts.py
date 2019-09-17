# -*- coding: utf-8 -*-

__author__ = 'Kjersti Rustad Kvisberg'
__email__ = 'kjkv@nmbu.no'


def letter_freq(txt):
    """Read input text and create dictionary with each letter, digit and symbol
    in input as keys, and how many times the repeated as values.
    :param txt: Input text.
    :return: Dictionary with letters etc. as keys and counting of each as values.
    """
    freq = dict()
    for element in txt.lower():
        if element not in freq.keys():
            freq[element] = 1
        else:
            freq[element] += 1
    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
