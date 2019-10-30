# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random
from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    """Contains methods needed to simulate the way home of a walker
    in a one-dimensional world. The walker can not move further
    to the left or right than the given limits.
    """
    def __init__(self, start, home, left_limit, right_limit):
        """Initialise the walker.

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
        """The walker takes one step to the left or to the right,
        as determined by drawing a random number 0 or 1. The walker's
        position and number of steps is updated accordingly. If walker reaches
        left or right limit, the move is not executed.
        """
        if random.randint(0, 1) == 0:
            if self.position > self.left_limit:
                self.position -= 1

        else:
            if self.position < self.right_limit:
                self.position += 1
        self.steps += 1


class BoundedSimulation(Simulation):
    """Simulates the way home of walkers in a one-dimensional world
    with boundaries."""
    def __init__(self, start, home, seed, left_limit, right_limit):
        """Initialise the simulation.

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of the walker's movement
        right_limit : int
            The right boundary of the walker's movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(self.start, self.home, seed)

    def single_walk(self):
        """Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken to reach home position.
        """
        bounded_walker = BoundedWalker(
            self.start, self.home, self.left_limit, self.right_limit
        )
        while not bounded_walker.is_at_home():
            bounded_walker.move()
        return bounded_walker.get_steps()


if __name__ == '__main__':
    num_sim = 20
    start_pos = 0
    home_pos = 20
    seed_val = 1
    left_limits = [0, -10, -100, -1000, -10000]
    print(
        f'Start position: {start_pos}, '
        f'Home position: {home_pos}, '
        f'Seed value: {seed_val}, '
        f'Right boundary: {home_pos}, '
    )
    for limit in left_limits:
        bounded_walker_sim = BoundedSimulation(
            start_pos, home_pos, seed_val, limit, home_pos
        )
        print(
            f'Left boundary: {limit}\n'
            f'Lengths of walks: {bounded_walker_sim.run_simulation(num_sim)}'
        )
