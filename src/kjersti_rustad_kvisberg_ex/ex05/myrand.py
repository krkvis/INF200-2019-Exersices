# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


class LCGRand:
    """Implementation of a linear congruential generator
    that returns random numbers.
    """
    def __init__(self, seed):
        """Initialise the class with given constants
        slope and congruence_class.

        Attributes
        ----------
        slope : int
            Constant given in ex. text, necessary for generation.
        congruence_class : int
            Constant given in ex. text, necessary for generation.
        random_number : int
            The generated number.

        Parameters
        ----------
        seed : int
            The seed that the generating is based on.
        """
        self.random_number = seed
        self.slope = 7**5
        self.congruence_class = 2**31 - 1

    def rand(self):
        """Generate a single random number based on a seed given by the user.

        Returns
        -------
        random_number : int
            The generated number.
        """
        self.random_number *= self.slope
        self.random_number %= self.congruence_class

        return self.random_number

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """Generate an infinite sequence of random numbers.

        Yields
        ------
        self.rand() : int
            A random number.
        """
        while True:
            yield self.rand()


class RandIter:
    """A random number iterator class."""
    def __init__(self, random_number_generator, length):
        """Initialise the class.

        Attributes
        ----------
        generator : method
            Takes no arguments and returns a random number.
        num_generated_numbers : int
            Number of numbers the class has returned.

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
        """Initialise the iterator.

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
        """Generate the next random number.

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
    rand_num_generator = LCGRand(1)
    for rand in rand_num_generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(rand_num_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
