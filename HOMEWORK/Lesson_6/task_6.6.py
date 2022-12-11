# Список рандомных чисел необходимо отсортировать его в виде,
# сначала четные, потом нечетные

data = [2, 5, 7, 34, 89, 93, 54, 32, 27, 276, 455, 132, 123, 3, 8, 53, 49, 76]

data.sort()
data_1 = []
data_2 = []

for i in data:
    if i % 2:
        data_1.append(i)
    else:
        data_2.append(i)
data = data_2 + data_1

print(data)
