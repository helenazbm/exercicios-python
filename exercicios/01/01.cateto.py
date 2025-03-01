# P1 - UFCG
# MARIA HELENA BARROS
# CACULO DO VALOR DE UM CATETO DO TRIANGULO RETANGULO

hipotenusa = float(input())
cateto1 = float(input())

cateto2 = (hipotenusa ** 2 - cateto1 ** 2) ** (1/2) 

print(f"hipotenusa: {hipotenusa:.2f}")
print(f"cateto 1: {cateto1:.2f}")
print(f"cateto 2: {cateto2:.2f}")