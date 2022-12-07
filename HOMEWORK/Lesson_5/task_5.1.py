# Вывести первые N чисел кратные M и больше K

show_num = int(input('How many numbers to display? '))
multip = int(input('Enter multiplicity: '))
min_num = int(input('Enter minimal value: '))

massiv = []
i = min_num + 1
while len(massiv) < show_num + 1:
    if i % multip:
        massiv.append(i)
    i += 1

print(massiv)
