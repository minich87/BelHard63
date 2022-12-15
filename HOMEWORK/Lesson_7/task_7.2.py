# На вход функции подается упорядоченный список чисел и некоторое число,
# реализовать бинарный поиск данного числа в списке

def binary_search(lst, number):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1

    while lst[mid] != number and low <= high:
        if number > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print('No value')
    else:
        print('ID =', mid)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

binary_search(data, 8)
