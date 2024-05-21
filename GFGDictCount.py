# https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/#

def dictcount(votes):
    dict1 = {}

    for x in votes:
        dict1[x] = votes.count(x)

    list1 = []
    for x, y in dict1.items():
        if y == max(dict1.values()):
            list1.append(x)
    print(sorted(list1)[0])


if __name__ == '__main__':
    votes = ["john", "johnny", "jackie",
               "johnny", "john", "jackie",
               "jamie", "jamie", "john",
               "johnny", "jamie", "johnny",
               "john","johnny", "john", "john", "john"]
    dictcount(votes)