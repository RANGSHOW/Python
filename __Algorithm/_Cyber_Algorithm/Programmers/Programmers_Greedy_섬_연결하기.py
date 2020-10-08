# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때, 필요한 최소 비용을 return

# n	costs										return
# 4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4

# 새롭게 연결하는 것이 아닌 만들어진 표(사이트 참조) 상태에서 가장 적은 금액을 찾기
# 1. 모든 섬이 연결되어야 한다
# 2. 금액을 우선 순위로 탐색


# class Island(object):
#     def __init__(self, island_num):
#         self.island_num = island_num
#         self.connected_island_list = [] # 리스트 요소는 Island 인스턴스
        
#     def generate_connection(target_island, cost):
#         # costs[i][1] = target_island
#         # costs[i][2] = cost
#         pass
    

    
# def solution(n, costs):
#     pass



# 모든 섬이 연결되어야하니까 처음에 '0'섬에서 부터 연결된 섬 중 금액이 작은 'X'섬 선택
# 'X'섬에서 연결된 금액이 가장 적은 섬 선택
# 반복

if __name__ == "__main__":
    
    n = 4
    connected_island_list = [0]

    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

    
    start_island = 0
    total_cost = 0
    while start_island < n - 1:
        min_cost = 1000000000
        target_island = 100000000
        for i in range(len(costs)):
            if costs[i][0] == start_island:
                if costs[i][2] < min_cost:
                    print("costs = {}".format(costs[i]))
                    min_cost = costs[i][2]
                    target_island = costs[i][1]
        total_cost += min_cost
        connected_island_list.append(target_island)
        start_island += 1
        
    print('연결된 섬의 목록은 {} 입니다.'.format(connected_island_list))
    print('최소 비용은 {} 입니다.'.format(total_cost))
        # 여기까지의 문제 섬1, 섬2는 직접적 연결이 없다
        # 허나 start_island가 1일 때 섬1에 연결된 섬이 섬2 밖에 없어서 연결됨