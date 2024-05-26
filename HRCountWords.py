# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
from collections import Counter


def countwords(list1):
    list2 = []

    dict1 = Counter(list1)

    print(len(dict1))

    for x, y in dict1.items():
        print(y, end =" ")


if __name__ == '__main__':
    n = 4
    list1 = ['bcdef', 'abcdefg','bcde','bcdef']

    countwords(list1)