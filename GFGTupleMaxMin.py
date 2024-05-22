# https://www.geeksforgeeks.org/python-maximum-and-minimum-k-elements-in-tuple/#

def tuplemaxmin(test_tup, k):
    list_tup = list(sorted(test_tup))
    list1 = []

    for x, y in enumerate(list_tup):
        if x < k or x >= len(list_tup) - k:
            list1.append(y)

    print(tuple(list1))

if __name__ == '__main__':
    test_tup = (3, 7, 1, 18, 9, 67, 0, 45, 21)
    k = 3
    tuplemaxmin(test_tup, k)