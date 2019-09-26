# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


def char_counts(textfilename):
    """Open file with the given filename, read the file content into a
        string, and count how often each character code occurs in the string.
        Return result as list.
    :param textfilename: file with text that the function reads.
    :return: list with number of occurrences of each character code (1-256)
        in textfilename.
    """
    text_to_read = open(textfilename).read()
    result = [0 for _ in range(256)]
    for char in text_to_read:
        char_code = ord(char)
        result[char_code] += 1
    return result


if __name__ == '__main__':
    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
