# number	k	return
# 1924	2	94
# 1231234	3	3234
# 4177252841	4	775841

# k개의 숫자만큼 뺀 문자열 중 가장 큰 값을 return 

def solution(number: str, k: int) -> str:
    pass
    
# >>> Method 1
# if __name__ == "__main__":
#     number = '4177252841'
#     k = 4
#     # len(number) - k 한 자리만큼의 숫자를 뽑는다 (큰 숫자 위주로 뽑기)
#     choice_num = len(number) - k
#     new_list = [x for x in zip(number, range(len(number)))]
#     new_list = sorted(new_list, reverse=True)[0:choice_num]
#     ordered_new_list = []
#     for val, idx in new_list:
#         ordered_new_list.append((idx, val))
#     print('선별된 값들 (정렬 전): \n', ordered_new_list)
#     ordered_new_list.sort()
#     print('선별된 값들 (정렬 후): \n', ordered_new_list)

#     answer = ''
#     for idx, val in ordered_new_list:
#         answer += val
#     print(answer)
#         # case3의 문제 : 4가 중복으로 뽑히면서 맨앞의 4가 같이 뽑힘


# >>> Method 2

def return_choosen_num_index(start_idx, need_nums) -> int:
    max_num = num_list[len(num_list) - 1]
    for i in range(len(num_list) - 1, start_idx - 1, -1):
        if len(num_list) - num_list.index(num_list[i]) > need_nums:
            if max_num < num_list[i]:
                max_num = num_list[i]
    return num_list.index(max_num)
        
        
        
        

if __name__ == "__main__":
    number = '4177252841'
    k = 4
    choose_num = len(number) - k
    num_list = [int(x) for x in number]
    idx_list = []
    
    idx_list.append(return_choosen_num_index(6, 3))
    
    for idx in idx_list:
        print('idx_list: ', idx_list)
        print('answer: ', num_list[idx], end='')
    
    
    # first_num으로 뽑한 것 뒤에 choice_num만큼 있다면 고르고 아니면 차등 큰수
    # 재귀적으로 해보자
    # 같은 수라면 앞에 있는 것 
    