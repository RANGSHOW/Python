import random

def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return

def selection_sort(array):
    pass

def insertion_sort(array):
    pass

def quick_sort(array, start, end):
    while start <= end:
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            while left <= end and array[left] <= array[pivot]:
                left += 1

            while right > start and array[right] >= array[pivot]:
                right -= 1

                array[right], array[pivot] = array[pivot], array[right]

            else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
                array[left], array[right] = array[right], array[left]

        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)
    


def count_sort(array):
    pass



if __name__ == "__main__":
    array = [3, 5, 6, 1, 11, 7, 9, 12, 0, 4, 2, 8, 10]
    
    func = bubble_sort
    print('Before', func.__name__,  'Sort: ', array)
    func(array)
    print('After', func.__name__, 'Sort:  ', array, '\n\n')
    
    func = selection_sort
    print('Before', func.__name__,  'Sort: ', array)
    func(array)
    print('After', func.__name__, 'Sort:  ', array, '\n\n')
    
    func = insertion_sort
    print('Before', func.__name__,  'Sort: ', array)
    func(array)
    print('After', func.__name__, 'Sort:  ', array, '\n\n')
    
    func = quick_sort
    print('Before', func.__name__,  'Sort: ', array)
    func(array, 0, len(array) - 1)
    print('After', func.__name__, 'Sort:  ', array, '\n\n')
    
    func = count_sort
    print('Before', func.__name__,  'Sort: ', array)
    func(array)
    print('After', func.__name__, 'Sort:  ', array, '\n\n')
    