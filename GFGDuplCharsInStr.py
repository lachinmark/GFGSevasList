# https://www.geeksforgeeks.org/python-find-duplicate-characters-string/#
def duplchars(str1):
    set1 = set()
    list1 = list(str1)

    for x in list1:
        list1.remove(x)
        if x in list1:
            set1.add(x)
    print(' '.join(set1))


def duplchars2(str1):
    x = filter(lambda x: str1.count(x)>1, str1)
    print(' '.join(set(x)))


if __name__ == '__main__':
    str1 = 'geeksforgeeeks'
    duplchars(str1)