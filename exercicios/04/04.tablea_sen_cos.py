import math

angulo_ini = float(input())
passo = float(input())
total_linhas = int(input())


print("|Angulo|   Seno|Cosseno|")
for valor in range(total_linhas):
    angulo = angulo_ini + valor * passo
    seno = math.sin(math.radians(angulo)) 
    cosseno = math.cos(math.radians(angulo))
    print(f"|{angulo:6}|{seno:.5f}|{cosseno:.5f}|")