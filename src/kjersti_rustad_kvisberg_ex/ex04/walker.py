# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"

import random as rand


class Walker:
    def __init__(self, x0, h):
        self.h = h
        self.x = x0
        self.steps = 0

    def move(self):
        if rand.randint(0, 1) == 0:
            self.x -= 1
        else:
            self.x += 1
        self.steps += 1

    def is_at_home(self):
        return Walker.get_position(self) == self.h

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.steps

    def walking_process(self):
        while Walker.is_at_home(self) is False:
            Walker.move(self)
        return Walker.get_steps(self)


if __name__ == '__main__':
    Ida = Walker(0, 2)
    print(Ida.walking_process())
