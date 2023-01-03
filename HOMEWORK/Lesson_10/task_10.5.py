with open('LONDON.txt', 'r', encoding='utf-8') as file:
    text = file.read()

with open('KEY.txt', 'r', encoding='utf-8') as file:
    key = file.read()

ord_text = [ord(el) for el in text]
bin_text = [[x for x in bin(el)[2:]] for el in ord_text]

ord_key = [ord(el) for el in key]
bin_key = [[x for x in bin(el)[2:]] for el in ord_key]


for i in range(len(bin_text)):
    for j in range(i):
        for x in range(len(bin_key)):
            for y in range(x):
                lst = [[0 if bin_text[i][j] == bin_key[x][y] else 1 for j in range(i)] for b in range(len(bin_text))]

print(lst)
