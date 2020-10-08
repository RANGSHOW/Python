# n		lost	reserve		return
# 5		[2, 4]	[1, 3, 5]	5
# 5		[2, 4]	[3]			4
# 3		[3]		[1]			2


# n -> 전체 학생
# return -> 수업을 들을 수 있는 학생



# solution(5, [2,3], [3,4])
# 위를 실행해서 결과값이 5가 나오지 않도록 수정해보세요~!


n = 5
lost = [2, 3]
reserve = [3, 4]

def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in range(len(lost)):
        
        for j in range(len(reserve)):

            if reserve[j] == lost[i]:
                reserve[j] = 100
                answer += 1
                

            elif abs(reserve[j] - lost[i]) == 1:
                reserve[j] = 100
                answer += 1
                
                
    return answer

print(solution(n, lost, reserve))


# 동일한 친구를 한 번 돌린다