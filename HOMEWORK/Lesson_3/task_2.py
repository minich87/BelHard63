# Пользователь вводит 3 числа, найти средне арифметическое с точностью 3.

from statistics import mean

num1 = None
while num1 == None:
    try:
        num1 = float(input('Enter number_1: '))
    except ValueError:
        print('Error! Enter only number.')

num2 = None
while num2 == None:
    try:
        num2 = float(input('Enter number_2: '))
    except ValueError:
        print('Error! Enter only number.')

num3 = None
while num3 == None:
    try:
        num3 = float(input('Enter number_3: '))
    except ValueError:
        print('Error! Enter only number.')

sum_nums = (num1, num2, num3)

print('Arithmetical mean:', round(mean(sum_nums), 3))
