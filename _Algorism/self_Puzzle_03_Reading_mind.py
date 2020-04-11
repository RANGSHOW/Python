import random

deck = ['A-C', 'A-D', 'A-H', 'A-S', '2-C', '2-D', '2-H', '2-S', '3-C', '3-D', '3-H', '3-S', 
        '4-C', '4-D', '4-H', '4-S', '5-C', '5-D', '5-H', '5-S', '6-C', '6-D', '6-H', '6-S', 
        '7-C', '7-D', '7-H', '7-S', '8-C', '8-D', '8-H', '8-S', '9-C', '9-D', '9-H', '9-S', 
        '10-C', '10-D', '10-H', '10-S', 'J-C', 'J-D', 'J-H', 'J-S', 'Q-C', 'Q-D', 'Q-H', 'Q-S',     
        'K-C', 'K-D', 'K-H', 'K-S']
num_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cls_list = [0] * 13
order_code = 'lmh', 'lhm', 'mlh' ,'mhl', 'hlm', 'hml'


class Card():
    def __init__(self, num, next = None):
        self.num = num
        self.next = next
        
def pick_five_cards():
    global cards
    cards = []
    for _ in range(5):
        cards.append(deck[random.randrange(0, 52)])

    for i in range(5):
        for j in range(i + 1, 5):
            if cards[i] == cards[j]:
                pick_five_cards()
            if cards[i][0] == cards[j][0]:
                    pick_five_cards()


cards = []
pick_five_cards()
for i in range(13):
    cls_list[i] = Card('{}'.format(num_list[i]))

for i in range(12):
    cls_list[i].next = cls_list[i + 1]
cls_list[12].next = cls_list[0]
    #/ 원형 연결리스트를 만들었다


#카드 순서 바꾸기 & '10'은 'T'로 바꿈
# cards = ['3-H', '10-D', 'K-D', '4-S', 'A-S']
for i in range(5):
    for j in range(i + 1, 5):
        if cards[i][-1] == cards[j][-1]:
            cards[i], cards[0] = cards[0], cards[i]
            cards[j], cards[4] = cards[4], cards[j]
        if cards[i][0] == '1' and cards[i][1] == '0':
            cards[i] = cards[i].replace('10', 'T')

for start_node in cls_list:
    if cards[0][0] == start_node.num:
        node = start_node
        node_cnt = 0
        while (node.num != cards[4][0]):
            node = node.next
            node_cnt += 1
if node_cnt > 6:
    node_cnt = 13 - node_cnt
    cards[i], cards[0] = cards[0], cards[i]
    cards[j], cards[4] = cards[4], cards[j]
    
#알파벳을 숫자로 변경
cards_val = []
for i in range(1, 4):
    cards_val.append(cards[i][0])
    
for i in range(3):
    if cards_val[i] == 'A': cards_val[i] = '1'
    if cards_val[i] == 'T': cards_val[i] = '10'
    if cards_val[i] == 'J': cards_val[i] = '11'
    if cards_val[i] == 'Q': cards_val[i] = '12'
    if cards_val[i] == 'K': cards_val[i] = '13'
    cards_val[i] = int(cards_val[i])
    
min_i = 0
max_i = 0
for i in range(3):
    if cards_val[i] < cards_val[min_i]:
        min_i = i
    if cards_val[i] > cards_val[max_i]:
        max_i = i
small = cards[min_i + 1]
big = cards[max_i + 1]
mid = cards[4 - (max_i + min_i)]

my_cards = cards
for i in range(1, 7):
    if node_cnt == i:
        code = order_code[i - 1]
        

if code[0] == 'l':    fir = small
elif code[0] == 'm':    fir = mid
elif code[0] == 'h':    fir = big
    
if code[1] == 'l':    sec = small
elif code[1] == 'm':    sec = mid
elif code[1] == 'h':    sec = big
    
if code[2] == 'l':    thr = small
elif code[2] == 'm':    thr = mid
elif code[2] == 'h':    thr = big
    
cards[1], cards[2], cards[3] = fir, sec, thr

for i in range(5):
    cards[i] = cards[i].replace('T', '10')
    
# print("숫자 거리:", node_cnt, "\n대응되는 거리 코드:", code)


print("order_code = 'lmh', 'lhm', 'mlh' ,'mhl', 'hlm', 'hml'")
for i in range(4):
    print("{} 번째 카드는 {}입니다.".format((i + 1), cards[i]))
    
my_fifth = input("그렇다면 5번째 카드는?:  ")
if my_fifth == cards[4]:
    print('개쯔네예~')
else:
    print('빡대가리네예~')
    print('정답은 {}라예~'.format(cards[4]))