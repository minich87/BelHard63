# Список чисел необходимо развернуть без использования метода revese
# и функции reversed, в так же доп. списка и среза

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def reverse_func(data):
    if len(data) == 1:
        return data
    return data[-1] + reverse_func(data[:-1])
    print(data)

reverse_func(data)

