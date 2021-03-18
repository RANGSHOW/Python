def necessary_skill_trees(skill, skill_trees) -> list:
    necessary_skill_tree_list = ['' for _ in range(len(skill_trees))]
    for j in range(len(skill_trees)):
            for k in range(len(skill_trees[j])):
                if skill_trees[j][k] in skill:
                    necessary_skill_tree_list[j] += '{}'.format(skill_trees[j][k])
    return necessary_skill_tree_list
                    
                    
def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    necessary_skill_tree_list = necessary_skill_trees(skill, skill_trees)
    print(necessary_skill_tree_list)
    for i in range(len(necessary_skill_tree_list)):
        if necessary_skill_tree_list[i].startswith(skill[0]):
            if necessary_skill_tree_list[i] in skill:
                answer += 1
        else:
            if necessary_skill_tree_list == '':
                answer += 1
    return answer


if __name__ == "__main__":
    
    skill = 'CBD'
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    print(solution(skill, skill_trees))
            


# skill의 모든 요소가 들어갈 필요는 없으나 순서대로 들어가야함
# skill의 요소를 제외하고 다른 알파벳은 자유
# skill[n]이 존재하기 위해 skill[0], skill[1], ... skill[n - 1]이 존재해야함

# 1 <= len(skill) <= 26
# 1 <= len(skill_trees) <= 20
# 2 <= len(skill_trees[n]) <= 26, 중복은 없다

# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
