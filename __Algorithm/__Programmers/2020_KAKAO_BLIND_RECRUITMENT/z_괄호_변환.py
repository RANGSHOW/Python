# p				result
# "(()())()"	"(()())()"
# ")("			"()"
# "()))((()"	"()(())()"


def is_balance(p):
    count = 0
    for single in p:
        if single == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False
        
def is_correct(p):
    count = 0
    for single in p:
        if single == '(':
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
    return True

def flip(p):
    p = p[1:-1]
    new_p = ''
    for single in p:
        if single == '(':
            new_p += ')'
        else:
            new_p += '('
    return new_p

def solution(p):
    
    if is_correct(p) == True:
        return p
    
    if p == '':
        return ''
    
    for i in range(1, len(p) + 1):
        if is_balance(p[0:i]) == True:
            u = p[0:i]
            v = p[i:]
            if is_correct(u) == True:
                return u + solution(v)
            
            else:    # u가 balance이지만 correct가 아닌 경우
                return '(' + solution(v) + ')' + flip(u)
                
if __name__ == "__main__":
    p = '()))((()'
    print(solution(p))