from pytest import mark
from classes import Ship, Board


def test_add_ship():
    test_board = Board()
    test_ship = Ship((0, 0), 3)
    test_board.add_ship(test_ship)
    assert test_board.shipList == [[(0, 0), (0, 1), (0, 2)]]
    assert test_board.contourList == {(0, 0), (0, 1), (0, 2), (0, 3),
                                       (1, 0), (1, 1), (1, 2), (1, 3)}


def test_add_ship2():
    test_board2 = Board()
    test_ship2 = Ship((2, 2), 2)
    test_ship3 = Ship((0, 1), 1)
    test_board2.add_ship(test_ship2)
    test_board2.add_ship(test_ship3)
    assert test_board2.shipList == [[(2, 2), (2, 3)], [(0, 1)]]
    assert test_board2.contourList == {(0, 0), (0, 1), (0, 2), (1, 0),
                                      (1, 1), (1, 2), (1, 3), (1, 4),
                                      (2, 1), (2, 2), (2, 3), (2, 4),
                                      (3, 1), (3, 2), (3, 3), (3, 4)}
    assert test_board2.shipAlive == 2


