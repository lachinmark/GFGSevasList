# https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/


def usingjoin(text):
    set1 = text.split('123')
    str2 = ' '.join(set1)
    print (str2)

def usingreplace(text):
    str2 = text.replace('123', ' ')
    print(str2)

if __name__ == '__main__':
    text = 'Geeks123For123Geeks'
    usingreplace(text)
