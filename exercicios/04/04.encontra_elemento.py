#unidade 04
#maria helena barros
#Encontra um elemento

numero = int(input())
lista_inteiros = input().split()

resposta = "não"

for x in lista_inteiros:
    if int(x) == numero:
        resposta = "sim"
        break

print(resposta)