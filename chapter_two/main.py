import random
def gen_random_l(n, _range=5000):
    l = []
    for _ in range(n):
        r = random.randrange(0, _range)
        l.append(r)

    return l

def find_smallest(l):
    smallest = l[0]
    smallest_index = 0
    for i in range(1, len(l)):
        if l[i] < smallest:
            smallest = l[i]
            smallest_index = i
    return smallest_index

# O(n^2)
def selection_sort(l):
    new = []
    for _ in range(len(l)):
        smallest = find_smallest(l)
        new.append(l.pop(smallest))

    return new

def main():
    l = gen_random_l(128)

    print(selection_sort(l))

if __name__ == "__main__":
    main()
