# Пользователь вводит 3 числа, подсчитать сколько из них положительных / отрицательных

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

nums = (num1, num2, num3)

count1 = 0
count2 = 0
for i in nums:
    if i > 0:
        count1 += 1
    elif i < 0:
        count2 += 1

print('Positive numbers:', count1)
print('Negative numbers:', count2)

