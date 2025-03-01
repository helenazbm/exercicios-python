fator = float(input())
valores = input().split()
lista_diferenca = []
soma = 0

for i in range(len(valores)-1):
    diferenca = abs(int(valores[i]) - int(valores[i+1]))
    lista_diferenca.append(diferenca)
    soma += diferenca

media = soma/ len(lista_diferenca)
limiar = media * fator

print(f"limiar: {limiar:.2f}")

for i in range(len(lista_diferenca)):
    if lista_diferenca[i] > limiar:
        print(f"variação {i+1:>2}: |{valores[i]:>2} - {valores[i+1]:>2}| = {lista_diferenca[i]}")