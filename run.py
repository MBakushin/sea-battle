from classes import *
def main():
    board = Board()
    comp = Computer()
    comp.gen_board()
    comp.board.output_field()
    print(comp.countOfExit)
    print(len(comp.board.shipList))
    
    
if __name__ == "__main__":
    main()
