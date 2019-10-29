# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random
from .walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home)

    def move(self):
        """
        The walker takes one step to the left or to the right,
        as determined by drawing a random number 0 or 1. The walker's
        position and number of steps is updated accordingly. If walker reaches
        left or right limit, the move is not executed.
        """
        if random.randint(0, 1) == 0:
            if self.position > self.left_limit:
                self.position -= 1
                self.steps += 1
        else:
            if self.position < self.right_limit:
                self.position += 1
                self.steps += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.seed = random.seed(seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(self.start, self.home, self.seed)


if __name__ == '__main__':
    walking_person = Walker(0, 5)
    position = walking_person.get_position()
