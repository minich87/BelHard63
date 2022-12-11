# В списке чисел, необходимо сместить список на N-число

n_shift = int(input('Enter N-shift: '))

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

data = data[n_shift:] + data[:n_shift]
print(data)

