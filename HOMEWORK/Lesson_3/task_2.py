# Пользователь вводит 3 числа, найти средне арифметическое с точностью 3.

num1 = 0
while num1 == 0:
    try:
        num1 = complex(input('Enter number_1: '))
    except ValueError:
        print('Error! Enter only number.')

num2 = 0
while num2 == 0:
    try:
        num2 = complex(input('Enter number_2: '))
    except ValueError:
        print('Error! Enter only number.')

num3 = 0
while num3 == 0:
    try:
        num3 = complex(input('Enter number_3: '))
    except ValueError:
        print('Error! Enter only number.')

sum_nums = num1 + num2 + num3

print('Arithmetical mean:', sum_nums / 3)
