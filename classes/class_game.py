from time import sleep
from classes.users_classes import *
from classes.exceptions import *


class Game:
    player = 1
    multiline_output = """Welcome in console game Sea-battle!
Each player have 7 ships: 1 ship with 3 cell, 2 ship with 2 cell
and 4 ship with 1 cell.
For fill your board with ships - input start coords in format:
first coord - horizontal coord,
second coord - vertical coord,
then choose direction for your ship:
hor - horizontal, vert - vertical.
Example: A 2
         vert.
Firstly you pick 3-cell ship, next two times you pick 2-cell ship and 
last four times you pick 1-cell ship.
After you gen your board, game will started. You and computer do turn after miss
of your opponent. 
Good luck!"""

    def __init__(self, comp: Computer, user: User):
        self.comp = comp
        self.user = user

    def greet(self):
        return self.multiline_output

    def loop(self):
        while True:
            print('Your board:')
            self.user.board.output_field()
            print()
            print('Computer board:')
            self.comp.board.output_field()
            if self.player % 2 == 0:
                choose_coords = self.comp.ask()
                if choose_coords:
                    if self.user.board.field[choose_coords[0]][choose_coords[1]] \
                            == self.user.board.shipMark:
                        self.user.board.field[choose_coords[0]][
                            choose_coords[1]] \
                            = self.user.board.shootMark
                        for i, ship in enumerate(self.user.board.shipList):
                            for dot in ship.dots():
                                if dot == choose_coords:
                                    self.user.board.shipList[i].hp -= 1
                                    if self.user.board.shipList[i].hp == 0:
                                        self.user.board.shipList.remove(ship)
                                        sleep(1)
                                        break
                        if len(self.user.board.shipList) == 0:
                            print("Computer win")
                            sleep(10)
                            exit()
                        sleep(1)
                    elif self.user.board.field[choose_coords[0]][
                        choose_coords[1]] == ' ':
                        self.user.board.field[choose_coords[0]][choose_coords[1]] \
                            = self.user.board.missMark
                        self.player += 1
                        sleep(1)
                        continue
            elif self.player % 2 != 0:
                choose_coords = self.user.ask()
                if choose_coords:
                    if self.comp.board.field[choose_coords[0]][choose_coords[1]] \
                            == self.comp.board.shipMark:
                        self.comp.board.field[choose_coords[0]][choose_coords[1]] \
                            = self.comp.board.shootMark
                        for i, ship in enumerate(self.comp.board.shipList):
                            for dot in ship.dots():
                                if dot == choose_coords:
                                    self.comp.board.shipList[i].hp -= 1
                                    if self.comp.board.shipList[i].hp == 0:
                                        self.comp.board.shipList.remove(ship)
                                        sleep(1)
                                        break
                        if len(self.comp.board.shipList) == 0:
                            print("You win")
                            sleep(3)
                            exit()
                        sleep(1)
                    elif self.comp.board.field[choose_coords[0]][
                        choose_coords[1]] == ' ':
                        self.comp.board.field[choose_coords[0]][choose_coords[1]] \
                            = self.comp.board.missMark
                        self.player += 1
                        sleep(1)
                        continue

    def start(self):
        print(self.greet())
        self.user.gen_board()
        self.comp.gen_board()
        self.loop()
