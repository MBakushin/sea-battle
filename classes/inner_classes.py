from copy import copy
from numpy import pad
from classes.exceptions import *

class Dot:
    """Class for define dot in tuple:
       x - horizontal coord,
       y - vertical coord
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._coords = (self._x, self._y)

    @property
    def coords(self):
        return self._coords

    def __eq__(self, other):
        tmp = other if isinstance(other, tuple) else other.coords
        return self.coords == tmp


class Ship:
    """Class for init ship class obj."""
    available_direction = ('hor', 'vert')

    def __init__(self, startCoords: tuple, length: int, direction: str = 'hor'):
        self.startCoords = startCoords
        self._lenght = length
        self._direction = direction
        self._hp = length

    def __repr__(self):
        return f"{self.__class__}: {self.dots()}"

    @property
    def startCoords(self):
        return self._startCoords

    @startCoords.setter
    def startCoords(self, value):
        self._startCoords = value

    def dots(self) -> list[tuple]:
        """Method return array with dot in tuple"""
        dotsList = [self.startCoords]
        if self._lenght > 1:
            if self._direction == 'hor':
                for i in range(1, self._lenght):
                    dotsList.append((self.startCoords[0], self.startCoords[1] + i))
            elif self._direction == 'vert':
                for i in range(1, self._lenght):
                    dotsList.append((self.startCoords[0] + i, self.startCoords[1]))
        return dotsList


class Board:
    HOR_VIEW = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}  # fill it
    VER_VIEW = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'}  # fill it
    shipMark = u'\u25a0'  # Unicode for black square
    shootMark = 'X'
    missMark = 'O'

    def __init__(self, hid=False, size=6, shipList=None,
                 contourList=None, shipAlive=0):
        self.__hid = hid
        self.field = [[' ' for i in range(size)] for i in range(size)]
        if shipList is None:
            shipList = []
        self.shipList = shipList
        if contourList is None:
            contourList = set()
        self.contourList = contourList
        self.shipAlive = shipAlive

    @property
    def shipList(self):
        return self._shipList

    @shipList.setter
    def shipList(self, value):
        self._shipList = value

    @property
    def shipAlive(self):
        return self._shipAlive

    @shipAlive.setter
    def shipAlive(self, value):
        self._shipAlive = value

    @property
    def contourList(self):
        return self._contourList

    @contourList.setter
    def contourList(self, value):
        self._contourList = value

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field = value

    @field.deleter
    def field(self):
        del self._field

    def __len__(self):
        return len(self._field)

    def add_ship(self, ship: Ship):
        """Method add ship class obj to Board"""
        self.shipList.append(ship)
        for i in range(len(ship.dots())):
            self.field[ship.dots()[i][0]][ship.dots()[i][1]] = self.shipMark
        self.fill_contour()
        self.shipAlive += 1

    def fill_contour(self):
        """Method complete contour array with coord"""
        self.tmp_field = pad(self.field, 1, mode='constant')
        for i in range(1, len(self.tmp_field) - 1):
            for j in range(1, len(self.tmp_field) - 1):
                for row in range(3):
                    if self.shipMark in self.tmp_field[i - 1 + row][j - 1:j + 2]:
                        self.contourList.add((i-1, j-1))
                        break

    def output_field(self):
        self.tmp_field = copy(self.field)
        if self.__hid:
            for i in range(len(self.tmp_field)):
                for j in range(len(self.tmp_field)):
                    if self.tmp_field[i][j] == self.shipMark:
                        self.tmp_field[i][j] = ' '

        print('    ', end='')
        for value in self.HOR_VIEW.values():
            print(value, end=' | ')
        print()
        print('- - - - - - - - - - - - - - ')
        for index, num in enumerate(self.tmp_field):
            row = ' | '.join(num)
            print(f'{self.VER_VIEW[index]} | {row} |')
            print('- - - - - - - - - - - - - - ')

    def out(self, dot):
        ...

    def shoot(self):
        ...
