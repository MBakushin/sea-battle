from classes.inner_classes import *
from classes.exceptions import *
from random import randrange, choice


def rerun_func(func):
    """Decorator to rerun func"""
    def wrapper(*args, **kwargs):
        count = 10
        while count:
            try:
                return func(*args, **kwargs)
            except GenBoardError:
                print('GenBoardError')
                count -= 1
                continue
        return "try again"
    return wrapper


class Player:
    lenShip = {0: 3, 1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1}

    def __init__(self, count=0):
        self.count = count

    def gen_board(self):
        ...


class User(Player):
    hor_coord_dict = {v: k for k, v in Board.HOR_VIEW.items()}
    ver_coord_dict = {v: k for k, v in Board.VER_VIEW.items()}
    def __init__(self, count=0, board=Board()):
        super().__init__(count=0)
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value: Board):
        self._board = value

    @rerun_func
    def gen_board(self):
        while self.count < len(self.lenShip):
            self.board.output_field()
            if len(self.board.contourList) == (len(self.board)**2):
                print("Can't add any ship, gen new board")
                break
            try:
                self.enter_coords = input('Enter coords: ').split()
                if len(self.enter_coords) != 2:
                    raise IncorrectInputCoord
                elif self.enter_coords[0] not in self.hor_coord_dict:
                    raise IncorrectInputCoord
                elif self.enter_coords[1] not in self.ver_coord_dict:
                    raise IncorrectInputCoord
                self.start_coords = (self.ver_coord_dict[self.enter_coords[1]],
                                     self.hor_coord_dict[self.enter_coords[0]])
                if self.start_coords in self.board.contourList:
                    raise ContourException
            except IncorrectInputCoord:
                print("Incorrect input coord ")
                continue
            except ContourException:
                print("Enter available coord")
                continue
            try:
                if self.count > 2:
                    self.direction = 'hor'
                else:
                    self.direction = input("Enter ship direction: ")
                    if self.direction not in Ship.available_direction:
                        raise IncorrectInputCoord
            except IncorrectInputCoord:
                print("Incorrect input direction ")
                continue
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
                print("Coords out of field or coords are not available")
                continue
            self.board.add_ship(self.ship)
            print(self.board.shipList)  # remove it
            print(len(self.board.contourList))  # remove it
            self.count += 1
        else:
            return True
        self.count = 0
        self.board = Board()
        raise GenBoardError


class Computer(Player):
    def __init__(self, count=0, countOfExit=0, board=Board(hid=True)):
        super().__init__(count=0)
        self.countOfExit = countOfExit
        self.board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value: Board):
        self._board = value

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
