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
        return self.x == self.h

    def get_postition(self):
        return self.x

    def get_steps(self):
        pass

    def waking_process(self):
        pass
