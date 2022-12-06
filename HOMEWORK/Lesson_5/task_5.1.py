# Вывести первые N чисел кратные M и больше K

show_numbers = int(input('How many numbers to display? '))
multiplicity = int(input('Enter multiplicity: '))
min_number = int(input('Enter minimal value: '))

for i in range(0, 100000):
    if i % multiplicity == 0 and i > min_number:
        print(i(range(show_numbers)))
