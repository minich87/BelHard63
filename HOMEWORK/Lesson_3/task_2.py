# Пользователь вводит 3 числа, найти средне арифметическое с точностью 3.

from statistics import mean

num1 = float(input('Enter number_1: '))
num2 = float(input('Enter number_2: '))
num3 = float(input('Enter number_3: '))

sum_nums = (num1, num2, num3)

print('Arithmetical mean:', round(mean(sum_nums), 3))
