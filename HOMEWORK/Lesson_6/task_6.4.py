# Список содержащий в себе различные типы данных, отфильтровать т.о.,
# чтобы остались только строки, без использования доп. списка

def filter_list(lst):
    for row in range(len(lst) - 1, -1, -1):
        if isinstance(lst[row], (int, float)):
            del lst[row]
        if isinstance(row, list):
            return filter_list(row)
    return lst

data = [0, 1, 2.2, 3, -4, 5, 6, True, 7, 8, 10, 5.66, 9, 'Hello', 8.76,
        'world', [9, 'Mersi!', 99, 34, False, 'Bingo!', 11], '!',
        ['hi', 365, 'earth', 3, 21, '!'], 'WELCOME', ',', 'to python']

print(filter_list(data))
