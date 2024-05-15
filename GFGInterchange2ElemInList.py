# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/


def intertwoels(list1, pos1, pos2):
    x = list1[pos1 - 1]
    list1[pos1-1] = list1[pos2-1]
    list1[pos2 - 1] = x

    print(list1)


def intertwoels2(list1, pos1, pos2):
    for i, x in enumerate(list1):
        if i == (pos1-1):
            elem1 = x
        if i == (pos2-1):
            elem2 = x

    list1[pos1-1], list1[pos2-1] = elem2, elem1
    print(list1)



if __name__ == '__main__':
    list1 = [23, 65, 19, 90, 86, 64, 93]
    pos1 = 2
    pos2 = 6

    intertwoels2(list1, pos1, pos2)