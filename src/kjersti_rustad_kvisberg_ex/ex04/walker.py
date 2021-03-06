# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random as rand


class Walker:
    """Simulates the way home of a walker in a one-dimensional world.

    Attributes
    ----------
    x : int
        The walker's current position.
    steps : int
        The number of steps the walker has taken to get to current position.
    """
    def __init__(self, x0, h):
        """
        Initialises Walker class with given parameters. The walker is at a
        position 'x' after taking 'steps' number of steps.

        Parameters
        ----------
        x0 : int
            The walker's initial position.
        h : int
            The walker's home and thus final position.
        """
        self.h = h
        self.x = x0
        self.steps = 0

    def move(self):
        """
        The walker takes one step to the left or to the right,
        as determined by drawing a random number 0 or 1. The walker's
        position and number of steps is updated accordingly.
        """
        if rand.randint(0, 1) == 0:
            self.x -= 1
        else:
            self.x += 1
        self.steps += 1

    def is_at_home(self):
        """
        Checks if the walker is home yet.

        Returns
        -------
        bool
            True if walker is at home, False if not.
        """
        return Walker.get_position(self) == self.h

    def get_position(self):
        """
        Returns current position of the walker.

        Returns
        -------
        x : int
            The walker's position.
        """
        return self.x

    def get_steps(self):
        """
        Returns the number of steps the walker has taken in total to get to
        current position.

        Returns
        -------
        steps : int
            Number of steps the walker has taken.
        """
        return self.steps

    def walking_process(self):
        """
        Checks if the walker is home yet, and makes a move if not.

        Returns
        -------
        steps : int
            Number of steps the walker has taken to reach home position.
        """
        while Walker.is_at_home(self) is False:
            Walker.move(self)
        return Walker.get_steps(self)


if __name__ == '__main__':
    home_positions = [1, 2, 5, 10, 20, 50, 100]
    num_simulations = 5
    initial_position = 0
    for home in home_positions:
        num_steps = []
        for _ in range(num_simulations):
            walker = Walker(initial_position, home)
            num_steps.append(walker.walking_process())
        print(f'Distance: {home:3} -> Path lengths: {sorted(num_steps)}')
