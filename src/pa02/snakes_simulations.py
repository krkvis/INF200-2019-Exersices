# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"

import random


class Board:
    def __init__(self, ladders=None, chutes=None, goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        return True

    def position_adjustment(self, position):
        return position


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0

    def move(self):
        self.position += 1


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        self.position += 1


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps

    def move(self):
        self.position += 1


class Simulation:
    def __init__(self, player_field, board=Board(), seed=4,
                 randomize_players=True):
        self.player_field = player_field
        self.board = board
        random.seed(seed)
        self.randomize_players = randomize_players
        self.results = []

    def single_game(self):
        return(1, 'Player')

    def run_simulation(self, num_games):
        for _ in range(num_games):
            self.results.append(self.single_game())

    def get_results(self):
        return self.results

    def winners_per_type(self):
        return {'Player': 1, 'ResilientPlayer': 1, 'LazyPlayer': 1}

    def durations_per_type(self):
        return {'Player': [1, 2, 3, 4], 'ResilientPlayer': [1, 2, 3, 4], 'LazyPlayer': [1, 2, 3, 4]}

    def players_per_type(self):
        return {'Player': 1, 'ResilientPlayer': 1, 'LazyPlayer': 1}



if __name__ == '__main__':
    board = Board()
    print(board.ladders)
