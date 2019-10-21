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
    def __init__(self, list_of_numbers):
        self.numbers = list_of_numbers
        self.counter = 0

    def rand(self):
        if self.counter == len(self.numbers):
            raise RuntimeError
        else:
            random_number = self.numbers[self.counter]
            self.counter += 1
            return random_number


if __name__ == '__main__':
