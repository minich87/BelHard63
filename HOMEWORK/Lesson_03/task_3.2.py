# Пользователь вводит 3 числа, найти средне арифметическое с точностью 3.

num1 = float(input('Enter number_1: '))
num2 = float(input('Enter number_2: '))
num3 = float(input('Enter number_3: '))

sum_nums = (num1 + num2 + num3) / 3

print('Arithmetical mean:', round(sum_nums, 3))
