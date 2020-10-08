class Linked(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def reduce_list(linked_list, index):
    linked_list[index - 1].data  -= linked_list[index - 1].next.data
    linked_list[index - 1].next = linked_list[index - 1].next.next

def show_list():
    print('\n')
    node = linked_list[0]
    while node:
        print(node.data, end=' ')
        node = node.next

def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * fact(num - 1)
        
if __name__ == "__main__":
    input_list = list((map(int, input().split())))
    list_num = input_list[0]
    final_num = input_list[1]
    linked_list = [0] * list_num
    
    # Generate Linked List 
    for i in range(list_num):
        linked_list[i] = Linked(input_list[i + 2])
    
    # Link
    for i in range(list_num - 1):
        linked_list[i].next = linked_list[i + 1]
    
    
# 5 8 12 10 4 3 5
# 아이디어 
#   1. 메모이제이션
#     reduce_idx 마다 특정 값이 들어갔을 때 나오는 값을 기억한다