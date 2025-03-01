hexadecimal = input()
lista_decimal = []

for e in hexadecimal:
    if e == "a":
        e = 10
    elif e == "b":
        e = 11
    elif e == "c":
        e = 12
    elif e == "d":
        e = 13
    elif e == "e":
        e = 14
    elif e == "f":
        e = 15
    lista_decimal.append(int(e))

lista_resposta = []
soma = 0

for i in range(len(lista_decimal)):
    valor = lista_decimal[i] * 16 ** (len(lista_decimal)-(int(i)+1))
    lista_resposta.append(valor)
    soma += int(valor)
    print(f"{lista_decimal[i]} * 16^{len(lista_decimal)-(int(i)+1)} = {lista_resposta[i]}")

print("---")
print(f"{hexadecimal}(16) = {soma}(10)")