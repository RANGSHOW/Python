import matplotlib.pyplot as plt
import random
import time

def bubble_sort(a_list):
    count = 0
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(0, i):
            if a_list[j] > a_list[j + 1]:
                count += 1
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return count
                
if __name__ == "__main__":
    my_list = []
    for i in range(1000):
        my_list.append(random.randrange(0, 1000))
    print("Before Sort:\n", my_list)
    plt.plot(my_list, c="g")
    count = bubble_sort(my_list)
    plt.plot(my_list, c="r")
    print("After Sort:\n",  my_list, "\nCount: {}".format(count))
