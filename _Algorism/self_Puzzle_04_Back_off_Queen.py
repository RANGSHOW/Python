import numpy as np
from random import randint

class Queen(object):
    def __init__(self, pos):
        self.pos = pos
        board[self.pos[0]][self.pos[1]] = 1   #Queen의 위치를 초기화와 함께 board에 '1'로 표시
        
        for i in range(queen):
            board[self.pos[0]][i] += 1
            board[i][self.pos[1]] += 1
            
        #대각선 추가해야해요
    
    
    
def show_board():
    for i in range(queen):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print('')
    print('\n')
    
    
def return_possible_pos() -> tuple:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
            else:
                return None

def make_queen():
    for queen in queen_list:
        if queen != 0:
            board[queen.pos[0]][queen.pos[1]] = 'Q' #chr(9813)
        else:
            break
    
if __name__ == "__main__":
    queen = 8
    board = np.zeros((queen, queen), dtype='int').tolist()
    queen_list = [0] * queen
#     queen_list[0] = Queen((randint(0, queen - 1), randint(0, queen - 1)))
    queen_list[0] = Queen((2, 2))
    make_queen()
    show_board()
    
    
#for i in range(1, 8):
#    if return_possible_pos:
#        queen_list[i] = Queen(return_possible_pos())
#    else:
#        print('Queen: "There is no place to go!"')
#    board()

