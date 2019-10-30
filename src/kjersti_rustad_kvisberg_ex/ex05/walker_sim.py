# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random


class Walker:
    """Contains methods needed to simulate the way home of a walker
    in a one-dimensional world."""
    def __init__(self, start, home):
        """Initialise the class.

        Attributes
        ----------
        position : int
            The walker's current position.
        steps : int
            The number of steps the walker has taken to get to current
            position.

        Parameters
        ----------
        start : int
            The walker's initial position.
        home : int
            The walker's home and thus final position.
        """
        self.home = home
        self.start = start
        self.position = start
        self.steps = 0

    def move(self):
        """The walker takes one step to the left or to the right,
        as determined by drawing a random number 0 or 1. The walker's
        position and number of steps is updated accordingly.
        """
        self.position += random.randint(0, 1) * 2 - 1
        self.steps += 1

    def is_at_home(self):
        """Checks if the walker is home yet.

        Returns
        -------
        bool
            True if walker is at home, False if not.
        """
        return self.get_position() == self.home

    def get_position(self):
        """Returns current position of the walker.

        Returns
        -------
        position : int
            The walker's position.
        """
        return self.position

    def get_steps(self):
        """Returns the number of steps the walker has taken in total to get to
        current position.

        Returns
        -------
        steps : int
            Number of steps the walker has taken.
        """
        return self.steps

    def reset(self):
        """Resets the walker's position to the start position,
        so the walker can be used again.
        """
        self.position = self.start


class Simulation:
    """Simulates the way home of walkers in a one-dimensional world."""
    def __init__(self, start, home, seed):
        """Initialise the simulation.

        Parameters
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.seed = random.seed(seed)
        self.start = start
        self.home = home

    def single_walk(self):
        """Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken to reach home position.
        """
        walker = Walker(self.start, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        """Run a set of walks, returns list of number of steps taken for each.

        Parameters
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':
    num_sim = 20
    start_pos = [0, 0, 0, 10, 10, 10]
    home_pos = [10, 10, 10, 0, 0, 0]
    seed_val = [12345, 12345, 54321, 12345, 12345, 54321]
    for i in range(6):
        walker_sim = Simulation(start_pos[i], home_pos[i], seed_val[i])
        print(f'Start position: {start_pos[i]:3}, '
              f'Home position: {home_pos[i]}, '
              f'Seed: {seed_val[i]},\n'
              f'Lengths of walks: {walker_sim.run_simulation(num_sim)}'
              )
