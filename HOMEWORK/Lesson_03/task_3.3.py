# Пользователь вводит имя, возраст, город.
# Тремя способами форматирования сформировать приветственное сообщение.

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')

# way_1
text1 = 'Hello! My name is ' + str(name) + '. I\'m ' + str(age) + ' years old. I\'m from ' + str(city) + '.'
print(text1)

# way_2
text2 = 'Hello! My name is {0}. I\'m {1} years old. I\'m from {2}.'.format(name, age, city)
print(text2)

# way_3
text3 = f'Hello! My name is {name}. I\'m {age} years old. I\'m from {city}.'
print(text3)
