#converte senha

palavra = input()
nova_palavra = ""
contador = 0

for indice in range(len(palavra)):
    
    if indice == 0:
        nova_palavra += palavra[indice]

    elif palavra[indice] == "a" or palavra[indice] == "A":
        nova_palavra += "4"
        contador += 1
    elif palavra[indice] == "e" or palavra[indice] == "E":
        nova_palavra += "3"
        contador += 1
    elif palavra[indice] == "i" or palavra[indice] == "I":
        nova_palavra += "1"
        contador += 1
    elif palavra[indice] == "o" or palavra[indice] == "O":
        nova_palavra += "0"
        contador += 1
    else:
        nova_palavra += palavra[indice]


print(f"{nova_palavra} ({contador} troca(s))")