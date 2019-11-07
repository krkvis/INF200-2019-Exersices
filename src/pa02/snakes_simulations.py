# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"


class Board:
    def __init__(self, ladders=None, chutes=None, goal=None):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        return True

    def position_adjustment(self, position):
        return position


class Player:
    def __init__(self, board):
        pass

    def move(self):
        pass


class ResilientPlayer(Player):
    def __init__(self):
        super().__init__(self, board)
        pass

    def move(self):
        pass


class LazyPlayer(Player):
    def __init__(self):
        super().__init__(self, board)
        pass

    def move(self):
        pass


class Simulation:
    def __init__(self, board, seed, bool_flag, players):
        pass

    def single_game(self):
        pass

    def run_simulation(self, num_games):
        pass

    def get_results(self):
        pass

    def winner_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass


if __name__ == '__main__':
    board = Board()
    print(board.ladders)
