import pytest
from classes import Ship, Board


def test_add_ship():
    test_board = Board()
    test_ship = Ship((0, 0), 3)
    test_board.add_ship(test_ship)
    assert test_board._shipList == [[(0, 0), (0, 1), (0, 2)]]
    assert test_board._contourList == {(0, 0), (0, 1), (0, 2), (0, 3),
                                       (1, 0), (1, 1), (1, 2), (1, 3)}

