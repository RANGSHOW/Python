## 다익스트라(데이크스트라) 최단 경로 알고리즘
    ### '각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다
    ### (1) 출발 노드를 설정한다
    ### (2) 최단 거리 테이블을 초기화한다
    ### (3) 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
    ### (4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
    ### (5) 위 과정에서 (3), (4) 번을 반복한다


    # 노드 개수 n, 링크 개수 m
    # 출발 노드 start
    # graph[i] == [시작노드, 도착노드, 비용]

n, m = 6, 11
start = 1
graph = [[1, 2, 2], [1, 3, 5], [1, 4, 1], [2, 4, 2], [2, 3, 3], [3, 2, 3], 
         [3, 6, 5], [4, 3, 3], [4, 5, 1], [5, 3, 1], [5, 6, 2]]
    
    

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    pass
    
    


import numpy as np
import pandas as pd


array = pd.array(([1, 2, 3]))
print(array)
if __name__ == "__main__":
    print(array)
    