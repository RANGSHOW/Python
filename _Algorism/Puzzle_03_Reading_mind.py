
deck = ['A-C', 'A-D', 'A-H', 'A-S', '2-C', '2-D', '2-H', '2-S', '3-C', '3-D', '3-H', '3-S', 
        '4-C', '4-D', '4-H', '4-S', '5-C', '5-D', '5-H', '5-S', '6-C', '6-D', '6-H', '6-S', 
        '7-C', '7-D', '7-H', '7-S', '8-C', '8-D', '8-H', '8-S', '9-C', '9-D', '9-H', '9-S', 
        '10-C', '10-D', '10-H', '10-S', 'J-C', 'J-D', 'J-H', 'J-S', 'Q-C', 'Q-D', 'Q-H', 'Q-S', 
        'K-C', 'K-D', 'K-H', 'K-S']

def AssistantOrdersCards():
    print("Cards are charcter strings as shown below.")
    print("Ordering is:", deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    for i in range(5):
        print("Please give card", i + 1, end = ' ')
        card = input("in above format")
        cards.append(card)
        #cards에 5장 모두 입력 받았다
        
        n = deck.index(card)    #iterable.index(elem: list, str, etc) -> int
        cind.append(n)
        #deck자체에서 cards안에 있는 5장의 순서를 찾아서 cind에 입력
        
        cardsuits.append(n % 4)    #4로 나누고 남은 나머지 == 카드의 모양
        cnumbers.append( n // 4)    #n을 4로 '정수 나누기' == 카드의 숫자
        
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pqirsuit = n % 4
def bubble_sort(num_list):
    for i in range(0, len(num_list) - 1):
        for j in range(i, len(num_list) - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
            
    

if __name__ == "__main__":
    import random
    number_list = []
    for i in range(22):
        number_list.append(random.randrange(0, 35))
    print(number_list)
    bubble_sort(number_list)
    print(number_list)
    print(number_list)
    
    
    
    for i in range(4):
        for i in range(4):
            print("{} X {} = {}".format(i, j, i * j))
            
    