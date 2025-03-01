media_ssp = float(input())

media_maior = [] 
while True:
    soma = 0
    entrada = input()
    if entrada == "fim":
        break

    ocorrencias = entrada.split()

    for num in ocorrencias:
        soma += int(num)

    media = soma / len(ocorrencias)

    if media < media_ssp / 2:
        break

    if media > media_ssp:
        media_maior.append(entrada)

for num in media_maior:
    print(num)