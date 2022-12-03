# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name", "email",
# а их значения будут введены пользователем

max_users = int(input('Enter amount users: '))

numbers_users = [i for i in range(0, max_users + 1)]

user = {'name': None, 'email': None}

users = dict.fromkeys(numbers_users, user)

i = 0
while i <= max_users:
    users[i]['name'] = input(f'Enter user №{i} name: ')
    users[i]['email'] = input(f'Enter user №{i} email: ')
    i += 1

print(users)
