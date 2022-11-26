# Пользователь вводит имя, возраст, город.
# Тремя способами форматирования сформировать приветственное сообщение.

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')

# way_1
print('Hello! My name is', name + '. I\'m', age, 'years old. I\'m from', city + '.')

# way_2
print('Hello! My name is {0}. I\'m {1} years old. I\'m from {2}.'.format(name, age, city))

# way_2
print('Hello! My name is {n}. I\'m {a} years old. I\'m from {c}.'.format(n=name, a=age, c=city))
