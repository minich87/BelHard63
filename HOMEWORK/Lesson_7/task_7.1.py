# На вход функции подается целое число N, сгенерировать треугольник паскаля глубиной N

def triangle_Pascal(N):
    row = [1]
    for i in range(N):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


triangle_Pascal(10)
