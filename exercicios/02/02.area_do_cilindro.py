import math

print("Cálculo da Superfície de um Cilindro")
print(3 * "-")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2
area = (2 * math.pi * (raio ** 2)) + ((2 * math.pi * raio) * altura)

print(3 * "-")
print(f"Área calculada: {area:.2f}")