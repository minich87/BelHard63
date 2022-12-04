# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name", "email",
# а их значения будут введены пользователем

max_users = int(input('Enter amount users: '))

users = {i: {'name': input(f'Enter name User_{i}: '),
             'email': input(f'Enter email User_{i}: ')}
         for i in range(0, max_users + 1)}

print(users)
