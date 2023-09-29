from classes import *
def main():
    user = User()
    comp = Computer()
    comp.gen_board()
    user.board.output_field()
    comp.board.output_field()
    game = Game(comp, user)

    
    
if __name__ == "__main__":
    main()
