capacidade = float(input("Capacidade de revestimento? "))

print()

print("== Dados do vão a revestir ==")
comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))
print()

area_total = 4*(largura * altura) + (comprimento * largura)
n_caixas = area_total / capacidade

print("== Resultados ==")
print(f"Área total a revestir: {area_total:.1f} m2")
print(f"Número de caixas: {n_caixas:.0f}")




                   