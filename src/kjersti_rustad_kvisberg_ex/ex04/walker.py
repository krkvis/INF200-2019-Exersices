# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random as rand


class Walker:
    def __init__(self, x0, h):
        """


        Parameters
        ----------
        x0
        h
        """
        self.h = h
        self.x = x0
        self.steps = 0

    def move(self):
        """


        Returns
        -------

        """
        if rand.randint(0, 1) == 0:
            self.x -= 1
        else:
            self.x += 1
        self.steps += 1

    def is_at_home(self):
        """


        Returns
        -------

        """
        return Walker.get_position(self) == self.h

    def get_position(self):
        """


        Returns
        -------

        """
        return self.x

    def get_steps(self):
        """


        Returns
        -------

        """
        return self.steps

    def walking_process(self):
        """


        Returns
        -------

        """
        while Walker.is_at_home(self) is False:
            Walker.move(self)
        return Walker.get_steps(self)


if __name__ == '__main__':
    home_positions = [1, 2, 5, 10, 20, 50, 100]
    num_simulations = 5
    initial_position = 0
    for home in home_positions:
        path_lengths = []
        for _ in range(num_simulations):
            walker = Walker(initial_position, home)
            path_lengths.append(walker.walking_process())
        print(f'Distance: {home:3} -> Path lengths: {path_lengths}')
