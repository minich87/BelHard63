# Вывести четные числа от 2 до N по 5 в строку.

upper_limit = None
while upper_limit is None:
    try:
        upper_limit = int(input('Enter upper limit: '))
    except ValueError:
        print('Please, enter integer!')

massif = []
for i in range(2, upper_limit+1):
    if i % 2 == 0:
        massif.append(i)

for i in range(0, len(massif), 5):
    print(massif[i: i + 5])
