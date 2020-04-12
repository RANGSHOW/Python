import numpy as np

class Queen(object):
    def __init__(self, pos):
        self.pos = pos
        board[self.pos[0]][self.pos[1]] = 1
        
def show_board():
    print('\n------------')
    print(board)
    print('------------\n')
    
if __name__ == "__main__":
    board = np.zeros((4, 4), dtype='int')
    queen_list = [0] * 8
    queen_list[0] = Queen((1, 2))
    show_board()