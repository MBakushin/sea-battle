from classes import *
def main():
    game = Game(Computer(), User())
    game.user.gen_board()
    game.comp.gen_board()
    game.greet()
    game.loop()

    
    
if __name__ == "__main__":
    main()
