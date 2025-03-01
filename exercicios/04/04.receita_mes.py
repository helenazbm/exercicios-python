lista_receita = []
lista_despesa = [] 
lista_lucro = []

mes = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

for meses in range(12):
    r, d= input().split()
    receita = float(r)
    lista_receita.append(receita)
    despesa = float(d)
    lista_despesa.append(despesa)

for indice in range(len(lista_receita)):
    lucro = lista_receita[indice] - lista_despesa[indice]
    lista_lucro.append(lucro)

for indice in range(len(mes)):
    print(f"{mes[indice]} {lista_lucro[indice]:4.1f}")