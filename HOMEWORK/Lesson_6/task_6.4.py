# Список содержащий в себе различные типы данных, отфильтровать т.о.,
# чтобы остались только строки, без использования доп. списка

data = [566, 'Hello', 8.76, 'world', (67, 'Mersi!', 899, 9), '!',
        ['hi', 365, 'earth', '!'], 'WELCOME', ',', 'to python']

for i in data:
    if i != str(i):
        data.remove(i)
print(data)
