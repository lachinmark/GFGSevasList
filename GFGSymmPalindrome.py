# https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

def symmetrical(str1):
    if len(str1) % 2 == 0:
        if str1[:divindex] == str1[divindex:]:
            print('The entered string is symmetrical')
        else:
            print('The entered string is NOT symmetrical')
    else:
        print('The entered string is NOT symmetrical')


def palindrome(str1):
    if len(str1) % 2 == 0:
        if str1[:divindex] == str1[divindex*2:divindex-1:-1]:
            print('The entered string is palindrome')
        else:
            print('The entered string is NOT palindrome')
    else:
        print('The entered string is NOT palindrome')


if __name__ == '__main__':
    str1 = 'massam'
    divindex = int(len(str1) / 2)
    symmetrical(str1)
    palindrome(str1)