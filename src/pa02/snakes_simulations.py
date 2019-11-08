# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"

import random


class Board:
    def __init__(self, ladders=None, chutes=None, goal=90):
        """Initializes board with default values"""
        self.goal = goal
        if ladders is None:
            self.ladders = [
                (1, 40), (8, 10), (36, 52), (49, 79), (65, 82), (68, 85)
            ]
        else:
            self.ladders = ladders

        if chutes is None:
            self.chutes = [
                (24, 5), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)
            ]
        else:
            self.chutes = chutes

    def goal_reached(self, position):
        """Returns True when player has reached or passed goal,
        False otherwise."""
        return position >= self.goal

    def position_adjustment(self, position):
        """Returns number of steps player must climb or fall when he encounters
        a ladder or chute. Zero is returned when player is in a position
        without ladders or chutes."""
        for ladder in self.ladders:
            if position == ladder[0]:
                return ladder[1] - ladder[0]

        for chute in self.chutes:
            if position == chute[0]:
                return chute[1] - chute[0]

        return 0


class Player:
    def __init__(self, board):
        """Initializes a player with given board."""
        self.board = board
        self.position = 0

    def move(self):
        """Updates players position with roll of die and potential move
        up ladder or down chute."""
        self.position += random.randint(1,6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        """Initializes a player with given board and extra steps."""
        super().__init__(board)
        self.extra_steps = extra_steps
        self.fell_down_a_chute = False

    def move(self):
        """Updates players position with roll of die, potential extra steps
         from last move and and potential move up ladder or down chute."""
        self.position += random.randint(1, 6)
        if self.fell_down_a_chute is True:
            self.position += self.extra_steps
        pos_adj = self.board.position_adjustment(self.position)
        if pos_adj <= 0:
            self.fell_down_a_chute = True
        else:
            self.fell_down_a_chute = False
        self.position += pos_adj


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        """Initializes player with a given board and number of dropped
        steps"""
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
