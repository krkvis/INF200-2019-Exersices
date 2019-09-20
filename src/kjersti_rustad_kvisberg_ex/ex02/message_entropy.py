# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import math


def letter_freq(txt):
    """Take input string and count how many times each letter, digit and symbol is repeated.
    :param txt: string that the function reads.
    :returns: dictionary with each character in txt as keys,
        and how many times they are repeated as values.
    """
    frequencies = dict()
    for element in txt:
        if element not in frequencies.keys():
            frequencies[element] = 1
        else:
            frequencies[element] += 1
    return frequencies


def entropy(message):
    """Compute the entropy of input message from given formula.
    :param message: string.
    :returns: entropy as number.
    """
    occurrence_dict = letter_freq(message)
    n = len(message)
    msg_entropy = 0
    for count in occurrence_dict.values():
        msg_entropy += ((count/n) * math.log2(count/n))
    return -msg_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
