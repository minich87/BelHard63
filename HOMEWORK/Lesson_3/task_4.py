# Пользователь вводит 3 числа, подсчитать сколько из них положительных / отрицательных

num1 = float(input('Enter number_1: '))
num2 = float(input('Enter number_2: '))
num3 = float(input('Enter number_3: '))

nums = str(num1) + str(num2) + str(num3)

neg_nums = nums.count('-')
pos_nums = 3 - neg_nums

print('Positive numbers:', pos_nums)
print('Negative numbers:', neg_nums)
