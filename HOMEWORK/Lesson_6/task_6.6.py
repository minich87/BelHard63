# Список рандомных чисел необходимо отсортировать его в виде,
# сначала четные, потом нечетные

def fist_even_numder(lst):
    lst.sort()
    lst_1 = []
    lst_2 = []
    for i in lst:
        if i % 2:
            lst_1.append(i)
        else:
            lst_2.append(i)
        lst = lst_2 + lst_1
    return lst


data = [2, 5, 7, 34, 89, 93, 54, 32, 27, 276, 455, 132, 123, 3, 8, 53, 49, 76]

print(fist_even_numder(data))
