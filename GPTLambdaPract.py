# Write a lambda function that takes a list of strings and returns a list of their lengths.
def lambdalistoflens(list1):
    list2 = list(map(lambda s: len(s), list1))
    print(list2)

# Write a lambda function that takes a list of numbers and returns a list of their squares.
def lambdasquares(listnums):
    list2 = list(map(lambda x : x**2, listnums))
    print(list2)

# Write a lambda function that takes a list of strings and returns a list of the strings reversed.
def lambdarevlists(liststr):
    list2 = list(map(lambda x : x[::-1], liststr))
    print(list2)

def lambdarevstr(str1):
    strlist = str1.split(' ')
    list2 = ' '.join(list(map(lambda x : x[::-1], strlist)))
    print(list2)

# Write a lambda function that takes a list of strings and filters out the strings that are not palindromes.
def lambdapalin(listpalin):
    list2 = list(filter(lambda x : x == x[::-1], listpalin))
    print(list2)

# Write a lambda function that sorts a list of tuples based on the second element of each tuple.
def lambdasecel(listtuples):
    list2 = sorted(listtuples, key = lambda x : x[1])
    print(list2)


if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    lambdalistoflens(list1)

    listnums = [1, 2, 3, 4]
    lambdasquares(listnums)

    str1 = 'will be in place'
    lambdarevstr(str1)

    liststr = ['hello', 'world']
    lambdarevlists(liststr)

    listpalin = ['radar', 'level', 'world', 'python']
    lambdapalin(listpalin)

    listtuples = [(1, 3),(1,5), (2, 1), (3, 2)]
    lambdasecel(listtuples)