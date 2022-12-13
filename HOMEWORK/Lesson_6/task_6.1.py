# Написать функцию перевода десятичного числа в двоичное и обратно,
# без использования функции int

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    for i in str(binary):
        decimal = decimal * 2 + int(i)
    return decimal


print(decimal_to_binary(213))
print(binary_to_decimal(11010101))
