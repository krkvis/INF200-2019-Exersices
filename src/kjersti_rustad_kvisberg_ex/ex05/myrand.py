# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


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
        """Initialises the class with given constants a and m.

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


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
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
        pass

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
        pass


if __name__ == '__main__':
    LCG_generator = LCGRand(1)
    print(LCG_generator.rand())
    print(LCG_generator.rand())
