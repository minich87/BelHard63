# В списке чисел, необходимо сместить список на N-число

dlina_list = int(input('Enter the length of the range of list: '))
n_shift = int(input('Enter N-shift: '))

data = []
for i in range(1, dlina_list + 1):
    data.append(i)

data = data[n_shift:] + data [:n_shift]
print(data)

