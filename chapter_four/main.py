def gen_ord_list(n, skip=0):
    l = [] 
    s = skip
    if n == 1:
        return [0,]
    for i in range(n - 1):
        if s != 0:
            s -= 1
        else: 
            l.append(i)
            s = skip
    return l

import random
def gen_random_l(n, _range=5000):
    l = []
    for _ in range(n):
        r = random.randrange(0, _range + 1)
        l.append(r)

    return l

def rec_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + rec_sum(arr[1:])

def rec_count(arr):
    if arr == []:
        return 0
    return 1 + rec_count(arr[1:])

def rec_max(arr):
    if arr == []:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        result = arr[mid]

        if result == item:
            return mid
        
        if result > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def rec_binary_search(arr, item):
    if arr == []:
        return None
    mid = (len(arr)) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        result = rec_binary_search(arr[mid + 1:], item)
        return result + mid + 1 if result is not None else None
    else:
        return rec_binary_search(arr[:mid], item)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

def main():
    # ordered = gen_ord_list(1)
    l = gen_random_l(10)
    # print(l)
    # print(ordered)
    print(rec_sum(l))
    # print(rec_count(l))
    print(rec_max(l))
    # print(rec_binary_search(ordered, 0))
    print(quick_sort(l))

if __name__ == "__main__":
    main()
