# В списке чисел для каждого элемента необходимо подсчитать сумму его соседей,
# для крайных чисел одним из соседей является число с противопожной строны

data = [2, 5, 7, 34, 89, 93, 54, 32, 27, 276, 455, 132, 123, 3, 8, 53, 49, 76]

for i in range(len(data)):
    print(data[i-1] + data[(i+1) % len(data)], end=' ')
