def executeSchedule(courses, selectionRule):
    selectedCourses = []
    while len(courses) > 0:
        selCourse = selectionRule(courses)
        selectedCourses.append(selCourse)
        courses = removeConflictingCourses(selCourse, courses)
    return selectedCourses

def removeConflictingCourses(selCourse, courses):
    nonConflictingCourses = []
    for s in courses:
        if s[1] <= selCourse[0] or s[0] >= selCourse[1]:
            nonConflictingCourses.append(s)
        return nonConflictingCourses
    
def shortDuration(courses):
    shortDuration = courses[0]
    for s in courses:
        if s[1] - s[0] < shortDuration[1] - shortDuration[0]:
            shortDuration = s
    return shortDuration

def leastConflicts(courses):
    conflictTotal = []
    for i in courses:
        conflictList = []
        for j in courses:
            if i == j or i[1] <= j[0] or i[0] >= j[1]:
                continue
            conflictList.append(courses.index(j))
        conflictTotal.append(conflictList)
    leastConflict = min(conflictTotal, key=len)
    leastConflictCourse = courses[conflictTotal.index(leastConflict)]
    return leastConflictCourse

def earliestFinishTime(courses):
    earliestFinishTime = courses[0]
    for i in courses:
        if i[1] < earliestFinishTime[1]:
            earliestFinishTime = i
    return earliestFinishTime

if __name__ == "__main__":
    
    courses = [(0, 2), (2, 4), (4, 6), (6, 8), (1, 3), 
               (3, 5), (5, 7), (1, 3), (1, 3), (5, 7), (5, 7)]
    
    mycourses = [[8, 9], [8, 10], [12, 13], [16, 17], [18, 19], [19, 20], 
                 [18, 20], [17, 19], [13, 20], [9, 11], [11, 12], [15, 17]]

    print('Shortest duration:', executeSchedule(mycourses, shortDuration))
    print('Earliest finish time:', executeSchedule(mycourses, earliestFinishTime))