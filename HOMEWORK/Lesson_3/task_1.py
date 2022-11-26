# Пользователь вводит предложение, двумя способами заменить пробелы на '_'.

string = input('Enter data: ')

# способ_1
print('Way_1:', string.replace(' ', '_'))

# способ_2
new_string = string.split()
print('Way_2:', '_'.join(new_string))
