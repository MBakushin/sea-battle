from classes.inner_classes import *
from classes.exceptions import *
from random import randrange, choice


def rerun_func(func):
    def wrapper(*args, **kwargs):
        count = 50
        while count:
            try:
                return func(*args, **kwargs)
            except GenBoardError:
                print('GenBoardError')
                count -= 1
                continue
    return wrapper


class Player:
    lenShip = {0: 3, 1: 2, 2: 2, 3: 1, 4:1, 5: 1, 6: 1}
    def __init__(self, board=Board(hid=True), count=0, countOfExit=0):  # board=Board(hid=True)
        self.board = board
        self.count = count
        self.countOfExit = countOfExit

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value: Board):
        self._board = value

    def gen_board(self):
        ...


class User(Player):
    def gen_board(self):
        ...


class Computer(Player):
    @rerun_func
    def gen_board(self):
        while self.count < len(self.lenShip):
            if self.countOfExit > 200:
                break
            self.start_x = randrange(len(self.board))
            self.start_y = randrange(len(self.board))
            self.start_coords = (self.start_x, self.start_y)
            if self.start_coords in self.board.contourList:
                self.countOfExit += 1
                continue
            self.direction = choice(Ship.available_direction)
            self.ship = Ship(self.start_coords, self.lenShip[self.count],
                        self.direction)
            try:
                for dots in self.ship.dots():
                    if dots in self.board.contourList:
                        raise ContourException
                    for dot in dots:
                        if dot >= len(self.board):
                            raise CoordsOutException
            except (ContourException, CoordsOutException):
                self.countOfExit += 1
                continue
            self.board.add_ship(self.ship)
            self.count += 1
        else:
            return True
        self.count = 0
        self.countOfExit = 0
        self.board = Board(hid=True)
        raise GenBoardError
