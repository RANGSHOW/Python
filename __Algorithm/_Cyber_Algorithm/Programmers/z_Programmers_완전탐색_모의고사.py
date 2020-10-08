first = [1, 2, 3, 4, 5] * 2000
second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

answers = [1,3,2,4,2]

correct_num = [0] * 3
for i in range(len(answers)):
    if answers[i] == first[i]:
        correct_num[0] += 1
    if answers[i] == second[i]:
        correct_num[1] += 1
    if answers[i] == third[i]:
        correct_num[2] += 1
answer = []
max_correct_num = max(correct_num)
for i in range(3):
    if correct_num[i] == max_correct_num:
        answer.append(i + 1)
print(answer)





# 모범 답안

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
