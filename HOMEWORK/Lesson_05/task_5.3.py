# Вывести четные числа от 2 до N по 5 в строку.

upper_limit = None
while upper_limit is None:
    try:
        upper_limit = int(input('Enter upper limit: '))
    except ValueError:
        print('Please, enter integer!')

massiv = []
for i in range(2, upper_limit+1):
    if i % 2 == 0:
        massiv.append(i)

for i in range(0, len(massiv), 5):
    print(massiv[i: i + 5])
