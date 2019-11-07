# -*- coding: utf-8 -*-

"""
Additional set of compatibility tests for PA02.
"""

__author__ = "Ida Lunde Naalsund, Kjersti Rustad Kvisberg"
__email__ = "idna@nmbu.no, kjkv@nmbu.no"

import snakes_simulations as ss


class TestBoard:
    def test_constructor_inputs(self):
        """Constructor with kw args assigns correct attribute values."""
        b = ss.Board()
        assert b.ladders == [(1, 40), (8, 10), (36, 52), (49, 79), (65, 82),
                             (68, 85)]
        assert b.chutes == [(24, 5), (42, 30), (56, 37), (64, 27), (74, 12),
                            (87, 70)]
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




