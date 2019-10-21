# -*- coding: utf-8 -*-

__author__ = "Kjersti Rustad Kvisberg"
__email__ = "kjkv@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        random_number = self.a * self.seed % self.m
        self.seed = random_number
        return random_number


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers

    def rand(self):
        pass


if __name__ == '__main__':
