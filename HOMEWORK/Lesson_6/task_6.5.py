# Список чисел необходимо развернуть без использования метода revese
# и функции reversed, в так же доп. списка и среза

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

j = -1
for i in range(int(len(data)/2)):
    data[i], data[j] = data[j], data[i]
    j -= 1
print(data)
