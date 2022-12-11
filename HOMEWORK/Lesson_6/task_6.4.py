# Список содержащий в себе различные типы данных, отфильтровать т.о.,
# чтобы остались только строки, без использования доп. списка

data = [0, 1, 2.2, 3, -4, 5, 6, True, 7, 8, 10, 5.66, 9, 'Hello', 8.76,
        'world', [9, 'Mersi!', 99, False, 'Bingo!', 11], '!',
        ['hi', 365, 'earth', 3, '!'], 'WELCOME', ',', 'to python']

for row in data:
    if isinstance(row, (int, float, bool)):
        data.remove(row)
    elif isinstance(row, list):
        for el in row:
            if isinstance(el, (int, float, bool)):
                row.remove(el)
print(data)
