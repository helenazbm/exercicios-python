contador = 0

while True:
    palavra = input()
    contador += 1

    vogal = 0
    consoante = 0
    for letra in palavra:
        if letra in "AaEeIiOoUu":
            vogal += 1
        else:
            consoante += 1
        
    if consoante > vogal:
        print(contador)
        break    