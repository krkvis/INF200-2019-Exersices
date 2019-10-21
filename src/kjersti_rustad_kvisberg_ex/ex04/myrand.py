# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        """
        Initialises the class with given constants a and m.

        Parameters
        ----------
        seed: int
            The seed that the LCG bases the generating on.
        """
        self.seed = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        """
        Uses a linear congruential generator to generate a random number based
        on a seed given by user.

        Returns
        -------
        random_number: int
            The generated number.
        """
        random_number = self.a * self.seed % self.m
        self.seed = random_number
        return random_number


class ListRand:
    def __init__(self, list_of_numbers):
        """
        Initialises the class with list given by user and a counter.

        Parameters
        ----------
        list_of_numbers: list
            List of numbers that will be returned one by one as random numbers.
        """
        self.numbers = list_of_numbers
        self.counter = 0

    def rand(self):
        """
        Returns random numbers from a list given by user.

        Returns
        -------
        random_number: int
            A random number drawn from the input list.
        """
        if self.counter == len(self.numbers):
            raise RuntimeError
        else:
            random_number = self.numbers[self.counter]
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
