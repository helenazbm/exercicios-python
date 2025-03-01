menor = int(input())
maior = int(input())
valor = int(input())

if valor == menor or valor == maior:
    resp = "dentro"

elif valor < menor:
    resp = "antes"

elif valor > menor and valor < maior:
    resp = "dentro"

else:
    resp = "depois"

print(resp)