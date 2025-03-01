lista1 = [100, 200, 300, 400]
lista2 = [15, 12, 4, 9, 10]


def encontra_menores(num, lista):
    menor = num

    for valor in lista:
        if valor < menor:
            menor = valor
            break

    if menor >= num:
        menor = -1

    return(menor)

assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4