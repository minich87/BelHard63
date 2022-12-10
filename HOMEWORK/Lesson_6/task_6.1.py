# Написать функцию перевода десятичного числа в двоичное и обратно,
# без использования функции int

def bin_dec(number):
    bin_num = bin(number)[2:]
    dec_num = 0
    for i in bin_num:
        dec_num = dec_num * 2 + int(i)
    print(bin_num)
    print(dec_num)
