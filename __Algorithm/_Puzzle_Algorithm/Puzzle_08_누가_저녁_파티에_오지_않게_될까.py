def Combination(n, guestList):
    allCombL = []
    for i in range(2 ** n):
        num = i
        cList = []
        for j in rnage(n):
            if num % 2 == 1:
                cList = [guestList[n - 1 - j]] + cList
            num = num // 2
        allCombL.append(cList)
    return allCombL

def removeBadCombinations(allCombL, dislikePairs):
    allGoodCombinations = []
    for i in allComL:
        good = True
        for j in dislikePairs:
            if j[0] in i and j[1] in i:
                good = False
        if good:
            allGoodCombinations.append(i)
    return allGoodCombinations

