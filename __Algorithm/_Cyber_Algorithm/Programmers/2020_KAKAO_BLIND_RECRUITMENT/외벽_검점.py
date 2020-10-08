# n		 weak				dist			result

# 12	[1, 5, 6, 10]		[1, 2, 3, 4]	2
# 12	[1, 3, 4, 9, 10]	[3, 5, 7]		1


# def solution(n, weak, dist):
#     answer = 0
#     return answer


class WallPoint(object):
    def __init__(self, wall_point=None):
        self.wall_point = wall_point
        self.last = None
        self.next = None
        
def init_wall_list(wall_num):
    global wall_list
    wall_list = [0] * wall_list
    wall_list
    for i in range(wall_num):
        wall_list.append(WallPoint(i + 1))
    
        
    
    

if __name__ == "__main__":
    n, weak, dist = input().split()
    init_wall_list(int(n))
    print(wall_list)