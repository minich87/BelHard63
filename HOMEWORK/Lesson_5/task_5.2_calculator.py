# Калькулятор
# Пользователь вводит первое число, действие и второе число

number_1 = None
while number_1 is None:
    try:
        number_1 = float(input('Enter number_1: '))
    except ValueError:
        print('Error! Need enter number!')

operator = input('Enter math operator (+, -, *, /, **, //, %): ')

number_2 = None
while number_2 is None:
    try:
        number_2 = float(input('Enter number_2: '))
    except ValueError:
        print('Error! Need enter number!')

if operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2
elif operator == '*':
    result = number_1 * number_2
elif operator == '/':
    result = number_1 / number_2
elif operator == '**':
    result = pow(number_1, number_2)
elif operator == '//':
    result = number_1 // number_2
elif operator == '%':
    result = number_1 % number_2
else:
    result = 'Error, incorrect operator entered!'

print('Result:', result)
