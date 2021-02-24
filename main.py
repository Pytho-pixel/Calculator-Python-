num_1 = int(input('Enter Number 1 - '))
operator = input('Enter operator - ')
num_2 = int(input('Enter Number 2 Here - '))
if operator == '+':
    print(num_1 + num_2)
elif operator == '-':
    print(num_1 - num_2)
elif operator == '*':
    print(num_1 * num_2)
elif operator == '/':
    print(num_1 / num_2)
else:
    print('Invalid Operator Entered')