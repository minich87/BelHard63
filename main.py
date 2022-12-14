numbers = [5, 6, 3, 6, 3, 65, 3, 6, 3, 6, 7, 21, 5, 3, 6, 4, 5, 658, 4, 68]
print(numbers.sort(key=lambda x: True if not x % 2 else False))
