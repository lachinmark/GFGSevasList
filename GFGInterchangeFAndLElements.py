# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

def interchangefal(list1):
    x = list1[0]
    y = list1[int(len(list1))-1]

    list1.remove(x)
    list1.remove(y)

    list1.insert(0, y)
    list1.insert(int(len(list1)), x)

    print(list1)

def interchangefal2(list1):

    smthg = list1[-1], list1[0]

    list1[0], list1[-1] = smthg

    print(list1)




if __name__ == '__main__':
    list1 = [12, 35, 9, 56, 24]
    interchangefal(list1) #why in second method it takes value from result of the first one

    interchangefal2(list1)