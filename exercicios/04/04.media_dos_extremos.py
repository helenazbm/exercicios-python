#alteração do valor atribuido ao maior

entrada = int(input())

menor = 9999999
maior = -999999
lista_numeros = []


for numeros in range(entrada):
    lista_numeros.append(int(input()))

for numero in lista_numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

media = (maior + menor) / 2

abaixo = 0
acima = 0

for numero in lista_numeros:
    if numero < media:
        abaixo += 1
    if numero > media:
        acima += 1


print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Média dos extremos: {media:.2f}")
print(f"{abaixo} número(s) abaixo da média")
print(f"{acima} número(s) acima da média")