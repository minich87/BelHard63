# Список чисел необходимо развернуть без использования метода revese
# и функции reversed, в так же доп. списка и среза

def reverse_list(lst):
    for i in range(int(len(lst) / 2)):
        lst[i], lst[~i] = lst[~i], lst[i]
    return lst


data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(reverse_list(data))
