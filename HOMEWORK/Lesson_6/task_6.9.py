# Словарь словарей, ключ внешнего словаря - id пользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у кого не указана почта (нет ключа email или
# значение этого ключа - пустая строка)

def filter_users(users):
    result = []
    for user in users.values():
        if not user.get('email'):
            result.append(user['name'])
    return result


users = {
    '0001': {'name': 'Andrey',
             'family': 'Modric',
             'email': 'a.modric@gmail.com'
             },
    '0002': {'name': 'Ann',
             'family': 'Koval',
             'phone': '+53462584001',
             'email': None
             },
    '0003': {'name': 'Ivan',
             'family': 'Rakitic',
             'phone': '+52356635841'
             },
    '0004': {'name': 'Cris',
             'family': 'Ronaldo',
             'phone': '+52352580410',
             'email': 'cr7@gmail.com'
             },
    '0005': {'name': 'Robert',
             'family': 'Levandovski',
             'phone': '+523631123041',
             },
    '0006': {'name': 'Viki',
             'family': 'Neymar',
             'phone': '',
             'email': 'v.ney@gmail.com'
             },
    '0007': {'name': 'Leo',
             'family': 'Messi',
             'phone': '+191035191035',
             'email': 'm19.@mail.net'
             },
}

print(filter_users(users))
