# https://www.geeksforgeeks.org/python-check-two-lists-least-one-element-common/


def checklistelscommon(list1, list2):
    for x in list1:
        if x in list2:
            return True
    return False



if __name__ == '__main__':
    a = [1, 2, 3, 4, 12]
    b = [5, 6, 7, 8, 9]

    print(checklistelscommon(a, b))