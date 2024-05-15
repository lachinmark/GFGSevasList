# https://www.geeksforgeeks.org/python-maximum-and-minimum-k-elements-in-tuple/


def extractbyindex(test_tup, k):
    tuplefinal = test_tup[:k-1] + test_tup[k:]
    print(tuplefinal)


if __name__ == '__main__':
    test_tup = (3, 7, 1, 18, 9)
    k = 2
    extractbyindex(test_tup, k)