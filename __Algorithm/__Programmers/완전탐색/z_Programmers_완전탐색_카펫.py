brown, yellow = [24, 24]

for w in range(3, int(brown / 2)):
    for h in range(3, w + 1):
        if (yellow == (w - 2) * (h - 2)):
            if (brown == 2 * (w + h) - 4):
                print([w, h])