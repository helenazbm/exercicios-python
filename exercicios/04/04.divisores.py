numero = int(input())

for valor in range(1, numero+1):
    if numero > valor and numero % valor == 0:
        print(valor)