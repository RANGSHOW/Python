def HowHardIsTheCrystal(n, d):
    r = 1
    while(r**d <= n):
        r = r + 1
        print('Radix chosen is', r)
        numDrops = 0
        floorNoBreak = [0] * d
        for i in range(d):
            for j in range(r - 1):
                floorNoBreak