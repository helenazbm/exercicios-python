coringa = int(input())
lista = input().split()

lista_diferenca = []

menor = 99999999999

for numero in lista:
    diferenca = abs(int(numero) - coringa)
    lista_diferenca.append(diferenca)

for valor in lista_diferenca:
    if valor < menor:
        menor = valor

print(f"menor distância absoluta: {menor}")

for indice in range(len(lista)):
    if lista_diferenca[indice] == menor:
        print(f"{indice}:{lista[indice]}")