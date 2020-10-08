original_num = '6130885671764050055578117823928343046132868869219005451882532150250807471953297259106016262852711376'
sum_of_digits = '336'
# original_num, sum_of_digits = input().split()
sum_of_digits = int(sum_of_digits)
print(len(original_num), sum_of_digits)
# original_num 보다 한자리수 낮은 애로 한 번 돌리고
# 같은 자리수 10, 100, 1000 등 에서부터 original_num - 1까지 돌려보자

# 1. 한자릿수 낮은 것 : 첫째 자리는 1 ~ 9, 나머지 자리는 0 ~ 9

# original_num - 1 자리로 만들 수 있는 세트를 구해서 순열로 나열하는 법을 쓰자

# 99 개의 숫자로 336 만드는 경우의 수 

# 싹다 돌면 너무 오래 걸린다 
# 어느 정도의 336을 만들 수 있는 리스트를 만들어서 끼워넣자

# 약 3.39 가 99개 있으면 336을 만들 수 있다

