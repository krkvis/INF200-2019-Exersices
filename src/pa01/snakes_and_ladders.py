# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"

import random as rd


def check_position_on_ladder_or_snake(position):
    """

    :param position: Players position on game board
    :return: New position
    """
    ladders_and_snakes = {1:40, 8:10, 36:52, 43:62, 49:79, 65:82, 68:85,
                          24:5, 33:3, 42:30, 56:37, 64:27, 74:12, 87:70
                          }

    if position in ladders_and_snakes.keys():
        return ladders_and_snakes[position]
    else:
        return position


def player_make_one_move(position):
    """

    :param position: Players position on game board
    :return: New position
    """
    position += rd.randint(1, 6)
    return check_position_on_ladder_or_snake(position)


def one_player_game():
    """

    :return: Number of throws needed
    for one player to finish game
    """
    player_position = 0
    num_moves = 0
    while player_position <= 90:
        player_position = player_make_one_move(player_position)
        num_moves += 1
    return num_moves


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    moves_per_player = []
    for player in range(num_players):
        num_moves = one_player_game()
        moves_per_player.append(num_moves)

    return min(moves_per_player)

def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbers of moves needed in each game.
    """
    moves_per_game = []
    for game in range(num_games):
        moves_per_game.append(single_game(num_players))

    return moves_per_game



def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """


if __name__ == "__main__":
