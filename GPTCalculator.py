
def calculator(input):
    # str1: object = input.replace(" ", "")
    # list1 = list(str1)
    # int_list = []
    # print(str1)
    #
    # for x in list1:
    #     if x in "+-/*":
    #         int_list = int_list.append(''.join(list1[:list1.index(x)]))


    stack = []
    current_number = 0
    operation = '+'
    for char in input + '+':
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in "+-*/":
            if operation == '+':
                stack.append(current_number)
                print(stack)
            elif operation == '-':
                stack.append(-current_number)
                print(stack)
            elif operation == '*':
                stack.append(stack.pop() * current_number)
                print(stack)
            elif operation == '/':
                stack.append(int(stack.pop() / current_number))
                print(stack)
            operation = char
            current_number = 0

    return sum(stack)


if __name__ == '__main__':
    input = " 14*3-50 / 2 "
    print(calculator(input))