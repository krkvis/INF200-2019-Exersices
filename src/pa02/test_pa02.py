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
        assert b.ladders == [
        (1, 40), (8, 10), (36, 52), (49, 79), (65, 82), (68, 85)
        ]
        assert b.chutes == [
        (24, 5), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)
        ]
        assert b.goal == 90


