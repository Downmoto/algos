def binary_search(l, item):
    low = 0
    high = len(l) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def gen_ord_list(n, skip=0):
    l = [0,] 
    s = skip
    for i in range(n - 1):
        if s != 0:
            s -= 1
        else: 
            l.append(i)
            s = skip
    return l

def main():
    l = gen_ord_list(128)
    print(binary_search(l, 3))
    print(binary_search(l, 13))

if __name__ == "__main__":
    main()
