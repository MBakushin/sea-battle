from pytest import mark
from classes import Computer


@mark.parametrize('comp, shipList', [(Computer(), 7),(Computer(), 7),
                                     (Computer(), 7), (Computer(), 7),
                                     (Computer(), 7), (Computer(), 7)])
def test_gen_board_computer(comp, shipList):
    comp.gen_board()
    assert len(comp.board.shipList) == shipList
