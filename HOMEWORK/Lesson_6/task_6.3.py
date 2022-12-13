# В списке чисел, необходимо сместить список на N-число

def offset_list(lst, offset):
    if abs(offset) < len(lst):
        return lst[-offset:] + lst[:-offset]
    if abs(offset) == len(lst):
        return lst
    if abs(offset) > len(lst):
        offset -= (offset // len(lst)) * len(lst)
        return lst[-offset:] + lst[:-offset]


print(offset_list([1, 2, 3, 4, 5, 6, 7], 3))
print(offset_list([1, 2, 3, 4, 5, 6, 7], 7))
print(offset_list([1, 2, 3, 4, 5, 6, 7], 11))

