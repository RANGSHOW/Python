heights = [1,5,3,6,7,6,5]
resp_list = [0] * len(heights)
for i in range(0, len(heights)):
    for j in range(i, -1, -1):
        if heights[i] < heights[j]:
            resp_list[i] = j + 1
            break
print(resp_list)