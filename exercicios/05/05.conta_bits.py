while True:
    bits = input()
    contagem = []
    contador = 0

    if bits == "0101010101":
        break

    novo_bits = bits + "0"

    for numero in novo_bits:
        if numero == "1":
            contador += 1
        if numero == "0":
            if contador != 0:
                contagem.append(contador)
            contador = 0
        if numero == "0":
            if contador == "0":
                print()

    resposta = ""
    for i in range(len(contagem)):
        if i == -1:
            resposta += str(contagem[i])
        else:
            resposta += f"{contagem[i]} "
        
    print(resposta)