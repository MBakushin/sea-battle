from classes.users_classes import *
from classes.exceptions import *


class Game:
    def __init__(self, comp: Computer, user: User):
        self.comp = comp
        self.user = user

    def greet(self):
        self.multiline_output = """Welcome in console game Sea-battle!
For fill your board with ships - input start coords in format:
first coord - horizontal coord,
second coord - vertical coord,
then choose direction for your ship:
hor - horizontal, vert - vertical.
Example: A 2
         vert.
Good luck!"""
        return self.multiline_output
