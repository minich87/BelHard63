# Пользователь вводит 3 числа, подсчитать сколько из них положительных / отрицательных

num1 = 0
while num1 == 0:
    try:
        num1 = float(input('Enter number_1: '))
    except ValueError:
        print('Error! Enter only number.')

num2 = 0
while num2 == 0:
    try:
        num2 = float(input('Enter number_2: '))
    except ValueError:
        print('Error! Enter only number.')

num3 = 0
while num3 == 0:
    try:
        num3 = float(input('Enter number_3: '))
    except ValueError:
        print('Error! Enter only number.')

nums = (num1, num2, num3)

for i in nums:
    if i > 0:
        i += 1
    print('Positive numbers:', i)
    if i < 0:
        i += 1
    print('Negative numbers:', i)