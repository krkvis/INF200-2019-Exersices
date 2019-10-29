# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

from .walker_sim import Walker, Simulation
import random


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

        super().__init__(self.start, self.home)


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
    