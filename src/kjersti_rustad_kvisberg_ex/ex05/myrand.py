# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random


class LCGRand:
    """Implementation of a linear congruential generator
    that returns random numbers.

    Attributes
    ----------
    slope : int
        Constant given in ex. text, necessary for generation.
    congruence_class : int
        Constant given in ex. text, necessary for generation.
    """
    slope = 7**5
    congruence_class = 2**31 - 1

    def __init__(self, seed):
        """Initialises the class with given constants
        slope and congruence_class.

        Parameters
        ----------
        seed : int
            The seed that the generating is based on.
        """
        self._hidden_state = seed

    def rand(self):
        """Generates a single random number based on a seed given by the user.

        Returns
        -------
        random_number : int
            The generated number.
        """
        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class

        return self._hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        pass
        # yield index, random_number


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate.
        """
        self.generator = random_number_generator.rand
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError(
                'Object can only be initialised as an iterator once.'
            )
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError(
                'Cannot call "next" before the object is'
                'initialised as an iterator.'
            )

        if self.num_generated_numbers == self.length:
            raise StopIteration(
                'The given amount of random numbers have been generated.'
            )

        self.num_generated_numbers += 1

        return self.generator()


if __name__ == '__main__':
    # LCG_gen = LCGRand(1)
    # print(LCG_gen.rand())
    # print(LCG_gen.random_sequence(3))


    rand_gen = RandIter(LCGRand(1), 3)
    iter(rand_gen)
    print(next(rand_gen))
    print(next(rand_gen))

    # random_number_generator = LCGRand(1)
    # for rand in random_number_generator.random_sequence(10):
    #   print(rand)

    # for i, rand in random_number_generator.infinite_random_sequence():
    #    print(f'The {i}-th random number is {rand}')
    #   if i > 100:
    #       break

