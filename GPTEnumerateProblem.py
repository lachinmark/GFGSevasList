# You have a list of integers, and you need to create a new list where each element is the sum of the original element and its index in the list. Use the enumerate function to achieve this.


def enumsumindex(list1):
    list2 = []

    for x,y in enumerate(list1):
        list2.append(x+y)

    print(list2)


if __name__ == '__main__':
    nums = [4, 3, 2, 1, 5, 6]

    enumsumindex(nums)