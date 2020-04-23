class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
def show_list(num):
    node = node_list[num]
    count = 0
    while count < len(prime_list):
        print(node.data, end=' ')
        node = node.next
        count += 1
        
if __name__ == "__main__":
    
    input_list = list(input().split())
    rotation_num = int(input_list[0])
    prime_list = input_list[1:]
    
    node_list = [0] * len(prime_list)
    
    node_list[0] = Node(prime_list[0])
    for i in range(len(prime_list) - 1):
        node_list[i + 1] = Node(prime_list[i + 1])
        node_list[i].next = node_list[i + 1]
        
    node_list[-1].next = node_list[0]  
    
    show_list(-rotation_num)
