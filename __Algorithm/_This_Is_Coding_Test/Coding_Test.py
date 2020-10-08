n, m = 5, 6
graph = [[1, 0, 1, 0, 1, 0], 
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
# dfs
    # 트리 형태로 작성한다

    
# 이동한 칸 수를 저장해서 그 result 를 return

# return False 를 사용하자


def dfs(row, col) -> int:
    if row < 0 or row >= n or col < 0 or col >= m:
        pass
    if graph[row, col] == 1:
        # 현재 위치가 길이라면
        
        
    
if __name__ == "__main__":
    