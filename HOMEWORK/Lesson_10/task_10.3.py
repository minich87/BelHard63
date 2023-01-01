with open('poem.txt', 'r', encoding='utf-8') as file:
    text = [line.split() for line in file if line.split()]

i = 1
for el in text:
    print(f'Количество слов в строке № {i}: ', len(el), end='     ')
    string = ''.join(el)
    print(f'Количество символов в строке № {i}: ', len(string))
    i += 1
