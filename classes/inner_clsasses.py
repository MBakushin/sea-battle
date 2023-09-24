import copy
import numpy as np


class Dot:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._coords = (self._x, self._y)

    @property
    def coords(self):
        return self._coords

    def __eq__(self, other):
        tmp = other if isinstance(other, tuple) else other.coord
        return self._coords == tmp


class Ship:
    available_direction = ('hor', 'vert')
    # start = DescShipCoords()

    def __init__(self, start: tuple, length, direction):
        self.start = start
        self._lenght = length
        self._direction = direction
        self._hp = length

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    def dots(self):
        dotsList = [self.start]
        if self._lenght > 1:
            if self._direction == 'hor':
                for i in range(1, self._lenght):
                    dotsList.append((self.start[0], self.start[1] + i))
            elif self._direction == 'vert':
                for i in range(1, self._lenght):
                    dotsList.append((self.start[0] + i, self.start[1]))
        return dotsList


class Board:
    class Board:
        HOR_VIEW = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}  # fill it
        VER_VIEW = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'}  # fill it
        shipMark = 'I'
        shootMark = 'X'
        missMark = 'O'
        _shipList = []
        _contourList = []
        _shipAlive = len(_shipList)

        def __init__(self, hid=False, size=6):
            self._hid = hid
            self._field = [[' ' for i in range(size)] for i in range(size)]

        @property
        def field(self):
            return self._field

        @field.setter
        def field(self, index, value):
            self._field[index] = value

        def __len__(self):
            return len(self._field)

        def add_ship(self):
            ...

        def contour(self):
            self._tmp_field = np.pad(self.field, 1, mode='constant')
            for i in range(1, len(self._tmp_field) - 1):
                for j in range(1, len(self._tmp_field) - 1):
                    for v in range(3):
                        if 'I' in self._tmp_field[i - 1 + v][j - 1:j + 2]:
                            self._contourList.append((i-1, j-1))

        def output_field(self):
            self._tmp_field = copy.copy(self.field)
            if self._hid == True:
                for i in range(len(self._tmp_field)):
                    for j in range(len(self._tmp_field)):
                        if self._tmp_field[i][j] == 'I':
                            self._tmp_field[i][j] = ' '

            print('    ', end='')
            for value in self.HOR_VIEW.values():
                print(value, end=' | ')
            print()
            print('- - - - - - - - - - - - - - ')
            for index, num in enumerate(self._tmp_field):
                row = ' | '.join(num)
                print(f'{self.VER_VIEW[index]} | {row} |')
                print('- - - - - - - - - - - - - - ')

        def out(self, dot):
            return dot

        def shoot(self):
            ...
