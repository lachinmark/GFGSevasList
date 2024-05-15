# https://www.geeksforgeeks.org/python-avoid-spaces-in-string-length/

def countnospace(text):
    z = 0
    for x in text:
        if x == ' ':
            z += 1

    print(int(len(text)) - z)





if __name__ == '__main__':
    text = 'Geeks For Geeks sfrgewrg ewrgae ger gerg e'
    countnospace(text)