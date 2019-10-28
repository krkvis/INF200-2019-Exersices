# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random


class Walker:
    """Simulates the way home of a walker in a one-dimensional world.

    Attributes
    ----------
    position : int
        The walker's current position.
    steps : int
        The number of steps the walker has taken to get to current position.
    """
    def __init__(self, start, home, seed):
        """
        Initialises Walker class with given parameters. The walker is at a
        position 'position' after taking 'steps' number of steps.

        Parameters
        ----------
        start : int
            The walker's initial position.
        home : int
            The walker's home and thus final position.
        seed : int
            Random generator seed.
        """
        self.home = home
        self.position = start
        self.steps = 0
        self.seed = seed

    def move(self):
        """
        The walker takes one step to the left or to the right,
        as determined by drawing a random number 0 or 1. The walker's
        position and number of steps is updated accordingly.
        """
        random.seed(self.seed)
        if random.randint(0, 1) == 0:
            self.position -= 1
        else:
            self.position += 1
        self.steps += 1

    def is_at_home(self):
        """
        Checks if the walker is home yet.

        Returns
        -------
        bool
            True if walker is at home, False if not.
        """
        return Walker.get_position(self) == self.home

    def get_position(self):
        """
        Returns current position of the walker.

        Returns
        -------
        position : int
            The walker's position.
        """
        return self.position

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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Parameters
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.walker = Walker(start, home, seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        return self.walker.walking_process()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Parameters
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        list_of_steps = []
        for _ in range(num_walks):
            list_of_steps.append(Simulation.single_walk(self))
        return list_of_steps


if __name__ == '__main__':
    home_positions = [1, 2, 5, 10, 20, 50, 100]
    num_simulations = 5
    initial_position = 0
    for home_position in home_positions:
        num_steps = []
        for _ in range(num_simulations):
            walker = Walker(initial_position, home_position)
            num_steps.append(walker.walking_process())
        print(f'Distance: {home_position:3} -> '
              f'Path lengths: {sorted(num_steps)}')
