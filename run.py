from classes import *
def main():
    user = User()
    user.gen_board()
    comp = Computer()
    comp.gen_board()
    user.board.output_field()
    comp.board.output_field()
    
    
if __name__ == "__main__":
    main()
