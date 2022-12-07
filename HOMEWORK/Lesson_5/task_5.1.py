# Вывести первые N чисел кратные M и больше K

show_numbers = None
while show_numbers is None:
    try:
        show_numbers = int(input('How many numbers to display? '))
    except ValueError:
        print('Error! Need enter integer!')

multiplicity = None
while multiplicity is None:
    try:
        multiplicity = float(input('Enter multiplicity: '))
    except ValueError:
        print('Error! Need enter number!')

min_number = None
while min_number is None:
    try:
        min_number = float(input('Enter minimal value: '))
    except ValueError:
        print('Error! Need enter number!')

massif = list(range(-5**10, 5**10))
result = []

for i in massif:
    if i % multiplicity == 0 and i > min_number:
        result.append(i)
print(result[:show_numbers])
