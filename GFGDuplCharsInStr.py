# https://www.geeksforgeeks.org/python-find-duplicate-characters-string/#
def duplchars(str1):
    list1 = list(str1)
    # print(list1)

    for x in list1:
        print(list1)
        list1.remove(x)
        set1 = set()
        print(list1)
        if x in list1:
            set1.add(x)

    print(set1)
    # Not sure why this is not working


def duplchars2(str1):
    x = filter(lambda x: str1.count(x)>1, str1)
    print(' '.join(set(x)))


if __name__ == '__main__':
    str1 = 'geeksforgeeeks'
    duplchars2(str1)