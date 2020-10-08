def no_conflicts(board, current, qindex, n):
    # qindex = current 열에 있는 퀸의 행의 위치값
    
    for j in range(current):
        if board[qindex][j] == 1:
            return False
        
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
            # '/ 방향' 대각선 충돌 검사
        
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current - k] == 1:
            return False
        k += 1
            # '\ 방향' 대각선 충돌 검사

    return True        
        # current 번 째의 열에 있는 퀸이 이전 열들에 있는 퀸들과 충돌 검사하는 함수


def four_queens(n=4):
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if no_conflicts(board, 1, j, n):
                for k in range(n):
                    board[k][2] = 1
                    if no_conflicts(board, 2, k, n):
                        for m in range(n):
                            board[m][3] = 1
                            if no_conflicts(board, 3, m, n):
                                print(board)
                            board[m][3] = 0
                        board[k][2] = 0
                    board[j][1] = 0
                board[i][0] = 0
            return 
        
        
        
        

if __name__ == "__main__":
    four_queens(4)
    