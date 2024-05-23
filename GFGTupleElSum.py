# https://www.geeksforgeeks.org/python-sum-of-tuple-elements/

def sumtupleel(test_tup):
    y = 0
    for x in test_tup:
        y += x
    print(y)

def sumtupleel2(test_tup):
    # res = sum(list(map(sum, list(test_tup))))
    res = list(map(sum, list(test_tup)))
    print(res)

def eventupleel(test_tup):
    print([x for x in test_tup if x % 2 == 0])


if __name__ == '__main__':
    test_tup = (3, 7, 1, 18, 9, 67, 0, 45, 21)
    test_tup2 = ([7, 8], [9, 1], [10, 7])
    eventupleel(test_tup)