courses = [(0, 2), (2, 4), (4, 6), (6, 8), (1, 3), 
           (3, 5), (5, 7), (1, 3), (1, 3), (5, 7), (5, 7)]

# IDEA: 제일 일찍 끝나는 수업을 고른다

def possible_course(last_selected_course) -> list:
    possible_courses = []
    for i in range(len(courses)):
        if courses[i][0] >= last_selected_course[1]:
            possible_courses.append(courses[i])
    return possible_courses
            
def select_course(possible_course_list: list) -> None:
    global final_courses
    min_end_time = 25
    min_end_time_course = []
    for i in range(len(possible_course_list)):
        if possible_course_list[i][1] < min_end_time:
            min_end_time_course = possible_course_list[i]
            print(possible_course_list[i][1])
            print(min_end_time_course)
            print('\n')S
    final_courses.append(min_end_time_course)
            
        
    # possible_course(num_courses[final_courses[-1]])
    
if __name__ == "__main__":
    final_courses = [(0, 0)]
    # 재귀함수로 해결해보자
    # 한 코스 추가 후 parameter + 1 해서 다시 호출
#     while possible_course(final_courses[-1]) != []:
    first_pos_course = possible_course(final_courses[-1])
    select_course(first_pos_course)
            
        