def solution(array, commands):
    answer = []
    for command in commands:
        print(command)
        temp_list = []
        temp_list = array[(command[0] - 1): (command[1])]
        selection_sort(temp_list)
        answer.append(temp_list[command[2] - 1])
    return answer

def selection_sort(alist):
    for i in range(len(alist)):
        min_idx = i
        for j in range(i, len(alist)):
            if alist[j] < alist[min_idx]:
                min_idx = j
        alist[min_idx], alist[i] = alist[i], alist[min_idx]
        

if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[4, 4, 1]]))
#     [[2, 5, 3], [4, 4, 1], [1, 7, 3]]



def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))