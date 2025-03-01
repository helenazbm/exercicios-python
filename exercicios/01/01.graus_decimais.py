# P1 -UFCG
# MARIA HELENA BARROS
# CONVERSÃO PARA GRAU DECIMAL 

grau = int(input())
minuto = int(input())
segundo = int(input())

grau_decimal = (grau * 3600  + minuto * 60 + segundo * 1) / 3600

print(f"graus = {grau_decimal:.4f}")