###self-made###
sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9),\
         (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]

times = []
for start, end in sched:
    for t in range(start, end):
        times.append(t)
time_set = set(times)
time_dict = {time: times.count(time) for time in time_set}
max_freq = max(time_dict.values())
for elem in time_set:
    if time_dict[elem] == 5:
        max_time = elem
print('Best time to attend the party is at',\
         max_time, 'o\'clock', ':', max_freq, 'celebrities will be attending!')

###textbook_method_1###: 연예인_존재_리스트[시간] == 연예인 수
sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9),\
         (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
sch
def best_time_to_party(schedule: list) -> None:
    start = schedule[0][0]
    end = schedule[0][1] 
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    count = celebrity_density(schedule, start, end)
    maxcount = 0
    for i in range(start, end + 1):
        if count[i] > maxcount:
            maxcount = count[i]
            time = i
    print('Best time to attend the party is at',\
     time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')
def celebrity_density(sched, start, end):
    count = [0] * (end + 1)    #len(count) == 13
    for i in range(start, end + 1):
        count[i] = 0
        for c in sched:
            if c[0] <= i and c[1] > i:    
                    #오는 시간(c[0])이 기준시간(i)보다 작거나 같아야하고, 가는 시간(c[1])이 기준시간보다 커야한다
                count[i] += 1
                    #'i'시간에 있는 손님수(count[i])를 1 증가시킨다
    return count

best_time_to_party(sched)

###textbook_method_2###:
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),\
         (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

def best_time_to_party_smart(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    sort_list(times)
    maxcount, time = choose_time(times)
    print('Best time to attend the party is at', \
          time, 'o\'clock', ':', maxcount, 'celecbrities will be attending!')
    
def sort_list(t_list: list) -> None:
    for ind in range(len(t_list) - 1):
        ism = ind
        for i in range(ind, len(t_list)):
            if t_list[ism][0] < t_list[i][0]:
                ism = i
        t_list[ind], t_list[ism] = t_list[ism], t_list[ind]
        
def choose_time(t_list):
    rcount = 0
    maxcount = time = 0
    for t in t_list:
        if t[1] == 'start':
            rcount = rcount + 1
        elif t[1] == 'end':
            rcount = rcount - 1
        if rcount > maxcount:
            maxcount = rcount
            time = t[0]
    return maxcount, time

if __name__ == "__main__":
    best_time_to_party_smart(sched2)

###self-made_textbook_method_2###
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),\
         (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
            #len(sched2) == 12
def best_time_to_party_smart(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
    sort_list(times)  
    maxcount, time = choose_time(times)
    print('Best time to attend the party is at', \
      time, 'o\'clock', ':', maxcount, 'celecbrities will be attending!')
    
def sort_list(t_list: list) -> None:
    for idx in range(len(t_list) - 1):
        min_idx = idx
        min_time = t_list[idx][0]
        for idx2 in range(idx + 1, len(t_list)):
            if t_list[idx2][0] < min_time:
                min_idx = idx2
                min_time = t_list[idx2][0]
        t_list[idx], t_list[min_idx] = t_list[min_idx], t_list[idx]
        
def choose_time(t_list) -> tuple:
    time_list = list(sorted(set(t_list[idx][0] for idx in range(len(t_list)))))
    time_list.insert(0, 'dummy')
    celeb_dict = {time_list[x]: 0 for x in range(len(time_list))}  
    current_time = time_list[0]
    for idx in range(len(t_list)):    #times: ('time', 'start_or_end')를 idx로 순회
        for idx2 in range(1, len(time_list)):    #idx2로 1 ~ 
            if t_list[idx][0] == time_list[idx2]:
                if t_list[idx][1] == 'start':
                    for idx3 in range(idx2, len(time_list)):
                        celeb_dict[time_list[idx3]] += 1

                else:
                    for idx3 in range(idx2, len(time_list)):
                        celeb_dict[time_list[idx3]] -= 1

    del celeb_dict['dummy']
    max_celeb = 0
    max_time = 0
    for time, num_of_celeb in celeb_dict.items():
        if num_of_celeb > max_celeb:
            max_celeb = num_of_celeb
            max_time = time
    return max_celeb, max_time

if __name__ == "__main__":
    best_time_to_party_smart(sched2)
