def no_conflicts(board, current, qindex, n):
    for j in range(current):
        if board[qindex][j] == 1:
            return False
        
    k = 1
    while qindex - k >= 0 and current - k >= 0:
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board