#atividade - unidade 03
#maria helena barros
# validação de triângulos

a = int(input())
b = int(input())
c = int(input())

perimetro = a + b + c 

if a < b + c and b < a + c and c < b + c:
    print("triangulo valido.", perimetro)

else:
    print("triangulo invalido.")

    