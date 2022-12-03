# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name", "email",
# а их значения будут введены пользователем

number_users = int(input("Enter amount users: "))

dict_key = (i for i in range(0, number_users+1))

name_dict2 = 'User_' + str(i for i in dict_key)

users = {}
users.fromkeys(dict_key, name_dict2)

user_key1 = 'name'
user_key2 = 'email'




print(dict_key)
print(name_dict2)