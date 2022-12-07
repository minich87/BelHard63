# Вывести первые N чисел кратные M и больше K

show_numbers = int(input('How many numbers to display? '))
multiplicity = int(input('Enter multiplicity: '))
min_number = int(input('Enter minimal value: '))

massiv = []
for i in range(min_number+1, 10**10):
    if i % multiplicity == 0:
        massiv.append(i)
        if len(massiv) == show_numbers:
            break

print(massiv)
