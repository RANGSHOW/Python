# budgets				M	return
# [120, 110, 140, 150]	485	127



def solution(budgets, M):
    upper_limited_budget = 0



    return upper_limited_budget

    



if __name__== "__main__":
    
    budgets = [120, 110, 140, 150]
    M = 485
    
    average_budget = sum(budgets) / len(budgets)
    
    
    for i in range(len(budgets)):
        if budgets[i] <= average_budget:      
            start_upper_budget = i
            
        elif budgets[-1] < average_budget:
            upper_limited_budget = budgets[-1]
            break
            
        elif budgets[0] > average_budget:
            upper_limited_budget = average_budget
            break
            
    start_upper_budget += 1
    upper_limited_budget = sum(budgets[i: -1]) / len(budgets[i + 1: -1]

    print(upper_limited_budget)
    
    
    
    #upper_limited_budgets = 127
    
    # average_budget > budgets[-1]:
        # 원하는대로 준다
        
    # average_budget < budgets[0]:
        # 모두에게 average_budget을 준다
        
    # 중간이라면:
        # average_budget >= budgets[i]:
            # 원하는대로 준다
        # average_budget < budgets[i]:
            # ( M - sum(budgets[0:i]) ) / len(budgets[i + 1:-1])