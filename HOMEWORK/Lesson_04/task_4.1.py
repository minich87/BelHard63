# Заполнить список степенями числа 2 (2^1, 2^n)

max_power = int(input('Enter max power: '))

user_list = [2**i for i in (range(1, max_power))]

print(user_list)
