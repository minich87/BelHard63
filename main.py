def bin_dec(number):
    bin_num = bin(number)[2:]
    print(type(bin_num))
    dec_num = 0
    for i in bin_num:
        dec_num = dec_num * 2 + int(i)
    print(bin_num)
    print(dec_num)

bin_dec(235)