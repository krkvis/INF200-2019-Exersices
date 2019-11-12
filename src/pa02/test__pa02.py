# -*- coding: utf-8 -*-

"""
Additional set of compatibility tests for PA02.
"""

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"

import snakes_simulations as ss


class TestBoard:
    def test_constructor(self):
        """Constructor with kw args assigns correct attribute values."""
        b = ss.Board()
        assert b.ladders == [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                             (65, 82), (68, 85)]
        assert b.chutes == [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                            (74, 12), (87, 70)]
        assert b.goal == 90

    def test_goal_reached(self):
        """Checks that True is returned when player has reached his goal"""
        b = ss.Board()
        position = 92
        assert b.goal_reached(position) == True

    def test_position_adjustment(self):
        """Checks that when climbing a ladder or falling down a chute, the
        correct number of steps moved is returned."""
        b = ss.Board(ladders=[(2, 5)], chutes=[(8, 3)])
        assert b.position_adjustment(2) == 3
        assert b.position_adjustment(8) == -5
        assert b.position_adjustment(6) == 0

class TestPlayer:
    def test_constructor(self):
        """Checks that class is initialized with position zero."""
        b = ss.Board()
        p = ss.Player(b)
        assert p.position == 0

    def test_move(self):
        """Checks that position has been changed, is not less than one,
        and not at the bottom of a ladder or top of a chute."""
        b = ss.Board(ladders=[(3, 7)], chutes=[(6, 5)])
        p = ss.Player(b)
        position = 2
        p.move()
        assert p.position != position
        assert p.position >= 1
        assert p.position != 3
        assert p.position != 6


class TestResilientPlayer:
    def test_constructor(self):
        """Checks that class is initialized with position zero."""
        b = ss.Board()
        p = ss.ResilientPlayer(b)
        assert p.position == 0

    def test_move(self):
        """Checks that position has been changed, is not less than one,
        and not at the bottom of a ladder or top of a chute."""
        b = ss.Board(ladders=[(3, 7)], chutes=[(6, 5)])
        p = ss.ResilientPlayer(b)
        position = 2
        p.move()
        assert p.position != position
        assert p.position >= 1
        assert p.position != 3
        assert p.position != 6

class TestLazyPlayer:
    def test_constructor(self):
        """Checks that class is initialized with position zero."""
        b = ss.Board()
        p = ss.LazyPlayer(b)
        assert p.position == 0

    def test_move(self):
        """Checks that position has been changed, is not less than one,
        and not at the bottom of a ladder or top of a chute."""
        b = ss.Board(ladders=[(3, 7)], chutes=[(6, 5)])
        p = ss.LazyPlayer(b)
        position = 2
        p.move()
        assert p.position != position
        assert p.position >= 1
        assert p.position != 3
        assert p.position != 6


class TestSimulation:
    def test_constructor_args(self):
        """Constructor with only two kw args works."""
        s = ss.Simulation(player_field=[ss.Player, ss.Player],
                          seed=5)
        assert isinstance(s, ss.Simulation)

    def test_play_round(self):
        """Checks that all players have moved during the round"""
        b = ss.Board()
        s = ss.Simulation(player_field=[ss.Player, ss.Player],
                          board=b, seed=123, randomize_players=True)
        s.setup_game()
        s.play_round()
        for p in s.player_instances:
            assert p.position >= 1

    def test_single_game(self):
        """Checks that the winning position is over 90"""
        b = ss.Board()
        s = ss.Simulation(player_field=[ss.Player, ss.Player],
                          board=b, seed=123, randomize_players=True)
        s.single_game()
        assert b.goal_reached(s.winning_player.position) is True

    def test_run_simulation(self):
        pass

    def test_get_results(self):
        s = ss.Simulation(player_field=[ss.Player, ss.Player],
                          board=ss.Board(), seed=123, randomize_players=True)
        s.run_simulation(2)
        assert type(s.get_results()) == list
        assert type(s.get_results()[0]) == tuple
