# words	queries	result
# ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# ["fro??", "????o", "fr???", "fro???", "pro?"]
# [3, 2, 4, 1, 0]

# '?'는 문자 하나. ?가 연속으로 등장하며
# "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드


def solution(words, queries):
    exp_list = []
    for query in queries:
        exp_list.append(query.replace('?', '\w'))
    
    answer = []
    
    for i in range(len(exp_list)):
        pat = re.compile(exp_list[i])
        cnt = 0
        queries_num = 0
        for word in words:
            if len(queries[i]) == len(word):
                if len(pat.findall(word)) == 1:
                    cnt += 1

        answer.append(cnt)
        
    return answer



if __name__ == "__main__":
    
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
    print(solution(words, queries))
    
    
    