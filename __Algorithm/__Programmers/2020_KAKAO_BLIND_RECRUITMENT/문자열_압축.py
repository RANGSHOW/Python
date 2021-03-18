# "aabbaccc"	7

# "ababcdcdababcdcd"	9

# "abcabcdede"	8

# "abcabcabcabcdededededede"	14
#     2abcabc2dedede

# "xababcdcdababcdcd"	17

def solution(s):
    compre_list = []
    for i in range(1, len(s) + 1):
        compre_list.append(compression(s, i))
    return min(compre_list)

def compression(s, div_num):
    
    s_list = list(s)
    div_list = []
    for _ in range(len(s) // div_num + 1):
        temp_elem = ''
        for _ in range(div_num):
            try:
                temp_elem += s_list.pop(0)
            except:
                break
        if temp_elem == '':
            break
        else:    
            div_list.append(temp_elem)
                
    fin_string = ''

    for i in range(len(div_list) - 1):
        if div_list[i] == div_list[i + 1]:
            div_list[i] = 1
            
    switch = 0
    while switch == 0:
        for i in range(len(div_list) - 1):
            if type(div_list[i]) == int and type(div_list[i + 1]) == int:
                div_list[i] = div_list[i] + div_list[i + 1]
                del div_list[i + 1]
                break
            else:
                switch = 1
        
    for i in range(len(div_list)):
        if type(div_list[i]) == int:
            div_list[i] = str(div_list[i] + 1)
    
    fin_string = ''.join(div_list)
    print("{} 단위: {}, 길이: {}".format(div_num, fin_string, len(fin_string)))
    return len(fin_string)
    
    
    
if __name__ == "__main__":
    s = "abcabcabcabcdededededdeddedede"
        # 15단위부터 렉
    print(compress(s, 13))
    