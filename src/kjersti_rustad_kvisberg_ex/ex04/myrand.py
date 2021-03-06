# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


class LCGRand:
    """Implementation of a linear congruential generator
    that returns random numbers.

    Attributes
    ----------
    a : int
        Constant given in ex. text, necessary for generation.
    m : int
        Constant given in ex. text, necessary for generation.
    """
    def __init__(self, seed):
        """Initialises the class with given constants a and m.

        Parameters
        ----------
        seed : int
            The seed that the generating is based on.
        """
        self.seed = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        """Generates a random number based on a seed given by the user.

        Returns
        -------
        random_number : int
            The generated number.
        """
        random_number = self.a * self.seed % self.m
        self.seed = random_number
        return random_number


class ListRand:
    """Generates random numbers from a list of numbers.

    Attributes
    ----------
    counter : int
        Number of numbers that have been returned from the list.
    """
    def __init__(self, list_of_numbers: list):
        """
        Initialises the class with list given by user and a counter.

        Parameters
        ----------
        list_of_numbers : list
            List of numbers that will be returned, one by one.
        """
        self.numbers_list = list_of_numbers
        self.counter = 0

    def rand(self):
        """
        Returns a number from the list.

        Raises
        ------
        RuntimeError :
            All numbers have been returned.

        Returns
        -------
        random_number : int
            Random number drawn from the input list.
        """
        if self.counter == len(self.numbers_list):
            raise RuntimeError('Empty list, all numbers have been returned.')
        else:
            random_number = self.numbers_list[self.counter]
            self.counter += 1
            return random_number


if __name__ == '__main__':
    LCG_generator = LCGRand(1)
    print(LCG_generator.rand())
    print(LCG_generator.rand())

    numbers_list = [1, 12, 5, 19, 2, 7, 16]
    list_generator = ListRand(numbers_list)
    print(list_generator.rand())
    print(list_generator.rand())
