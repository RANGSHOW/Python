import numpy as np
from random import randint

class Queen(object):
    def __init__(self, pos):
        self.pos = pos
        board[self.pos[0]][self.pos[1]] = 1   #Queen의 위치를 초기화와 함께 board에 '1'로 표시
        
def show_board():
    print('---------------')
    for i in range(queen):
        for j in range(len(board[i])):
            print(board[i, j], end=' ')
        print('')
    print('---------------')


    
    
    
if __name__ == "__main__":
    queen = 8
    board = np.zeros((queen, queen), dtype='int')
    queen_list = [0] * queen
    
    queen_list[0] = Queen((randint(0, queen - 1), randint(0, queen - 1)))
    
    show_board()

    

