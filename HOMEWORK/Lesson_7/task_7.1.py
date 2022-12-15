# На вход функции подается целое число N, сгенерировать треугольник паскаля глубиной N

def create_triangle(N):
    row = [1]
    for i in range(N):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


create_triangle(10)
