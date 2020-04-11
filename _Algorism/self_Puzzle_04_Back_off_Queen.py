#Queens
import random
from pprint import pprint




#첫번쨰 Queen은 랜덤으로 하자

def show():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("({},{})".format(i, j), end = ' ')
        print("\n")
        
def get_first_queen():
    return (randrange(0, queen_num), randrange(0, queen))

def increase_queen(q_idx: tuple) -> None:
    board[q_idx[0]][q_idx[1]] += 1
    
def increase_rows_and_cols(q_idx):
    for i in range(queen_num):
        board[q_idx[0]][i] += 1
        board[i][q_idx[1]] += 1
        
def increase_down_cross(q_idx):
    for i in range(q_idx[0] + 1, queen_num):
        board[i][q_idx[1] - (i - 2)] += 1
        board[i][q_idx[1] + (i - 2)] += 1

def increase_up_cross(q_idx):
    for i in range(q_idx[0] - 1, 0, -1):
        board[i][q_idx[1] - i] += 1
        board[i][q_idx[1] + i] += 1

def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = '   ')
        print('\n')
        


if __name__ == "__main__":
    queen_num = 5 #이 변수에 따라 board와 queen_num이 변화된다
    
    board = [[0] * queen_num for _ in range(queen_num)]
    show()
    
    fir_q_idx = (2, 2)
    
    increase_queen(fir_q_idx)
    increase_rows_and_cols(fir_q_idx)
    increase_down_cross(fir_q_idx)
    increase_up_cross(fir_q_idx)
    print_board()
    
    
    
    

