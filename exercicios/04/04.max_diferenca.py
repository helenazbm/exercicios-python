quantidade = int(input())
elementos = []

maior = -999999 

for x in range(quantidade):
    elementos.append(float(input()))

for i in range(len(elementos)-1):
    diferenca = abs(elementos[i] - elementos[i+1])
    if diferenca > maior:
        maior = diferenca
        valor = float(elementos[i])
        valor2 = float(elementos[i+1])
    
print(f"{valor} e {valor2}")