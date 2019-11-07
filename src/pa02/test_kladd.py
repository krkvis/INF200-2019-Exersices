
import snakes_simulations as ss
import pytest

class TestBoard:
    """
    Tests for Board class.
    """

    def test_constructor_default(self):
        """Default constructor callable."""
        b = ss.Board()
        assert isinstance(b, ss.Board)

    def test_constructor_args(self):
        """Constructor with unnamed arguments callable."""
        b = ss.Board([(1, 4), (5, 16)], [(9, 2), (12, 3)], 90)
        assert isinstance(b, ss.Board)

    def test_constructor_named_args(self):
        """Constructor with kw args callable."""
        b = ss.Board(ladders=[(1, 4), (5, 16)], chutes=[(9, 2), (12, 3)], goal=90)
        assert isinstance(b, ss.Board)

    def test_goal_reached(self):
        """goal_reached() callable and returns bool"""
        b = ss.Board()
        assert isinstance(b.goal_reached(1), bool)

    def test_position_adjustment(self):
        """position_adjustment callable and returns number"""
        b = ss.Board()
        assert isinstance(b.position_adjustment(1), (int, float))
