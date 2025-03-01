seq = input().split()
fator = int(input())

cont = 0
lista_pares = []

for indice in range(len(seq)-1):
    if int(seq[indice]) * fator == int(seq[indice+1]) or int(seq[indice]) == fator * int(seq[indice+1]):
        cont += 1
        lista_pares.append(f"{int(seq[indice])} {int(seq[indice+1])}")


print(f"{cont} par(es)")

for pares in lista_pares:
    print(pares)