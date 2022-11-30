# Пользователь вводит 3 числа, подсчитать сколько из них положительных / отрицательных

num1 = float(input('Enter number_1: '))
num2 = float(input('Enter number_2: '))
num3 = float(input('Enter number_3: '))

num1_is_positive = num1 > 0
num1_is_negative = num1 < 0
num2_is_positive = num2 > 0
num2_is_negative = num2 < 0
num3_is_positive = num3 > 0
num3_is_negative = num3 < 0

positive_nums = int(num1_is_positive) + int(num2_is_positive) + int(num3_is_positive)
negative_nums = int(num1_is_negative) + int(num2_is_negative) + int(num3_is_negative)

print('Positive numbers:', positive_nums)
print('Negative numbers:', negative_nums)
