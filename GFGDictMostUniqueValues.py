# https://www.geeksforgeeks.org/python-key-with-maximum-unique-values/


def dictuniqvalue(test_dict):
    len_list = []

    for x, y in test_dict.items():
        len_list.append(len(set(y)))

    max_len = max(len_list)

    for x, y in test_dict.items():
        if len(set(y)) == max_len:
            print(x)


def dictuniqvalue2(test_dict):
    max_len = 0
    max_key = None

    for x in test_dict:
        if len(set(test_dict[x])) > max_len:
            max_len = len(set(test_dict[x]))
            max_key = x
    print(max_key)


if __name__ == '__main__':
    test_dict = {"Gfg": [5, 7, 9, 4, 0], "is": [6, 7, 4, 3, 3, 0, 5], "Best": [9, 9, 6, 5, 5]}
    dictuniqvalue2(test_dict)