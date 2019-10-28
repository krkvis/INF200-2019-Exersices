# -*- coding: utf-8 -*-

"""
Acceptance test suite for EX05.
Your code should pass these tests before submission.
"""

from .walker_sim import Walker, Simulation
#from .bounded_sim import BoundedWalker, BoundedSimulation
#from .myrand import LCGRand

__author__ = "Hans Ekkehard Plesser"
__email__ = "hans.ekkehard.plesser@nmbu.no"


def test_walker():
    """Test that Walker class can be used as required."""

    start, home = 10, 20
    w = Walker(start, home)
    assert not w.is_at_home()
    w.move()
    assert w.get_position() != start
    w.move()
    assert w.get_steps() == 2


def test_simulation():
    """Test that Simulation class can be used as required."""

    start, home, seed, n_sim = 10, 20, 12345, 5
    s = Simulation(start, home, seed)
    assert s.single_walk() > 0
    r = s.run_simulation(n_sim)
    assert len(r) == n_sim
    assert all(rs > 0 for rs in r)
