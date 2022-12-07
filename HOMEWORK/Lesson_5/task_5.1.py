# Вывести первые N чисел кратные M и больше K

show_numbers = int(input('How many numbers to display? '))
multiplicity = float(input('Enter multiplicity: '))
min_number = int(input('Enter minimal value: '))

result = []
for i in range(min_number+1):
    if i % multiplicity == 0:
        result.append(i)
print(result[:show_numbers])
