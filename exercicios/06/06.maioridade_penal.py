
def maioridade_penal(nomes, idades):
    nomes = nomes.split()
    idades = idades.split()
    nomes_maiores = []
    resposta = ""

    for i in range(len(idades)):
        if int(idades[i]) >= 18:
            nomes_maiores.append(nomes[i])
        else:
            resposta = ""

    for i in range(len(nomes_maiores)):
        if i == len(nomes_maiores) - 1:
            resposta += f"{nomes_maiores[i]}"
        else:
            resposta += f"{nomes_maiores[i]} "

    return resposta

assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
assert maioridade_penal("a b c", "1 5 7") == ""
assert maioridade_penal("j k l", "18 28 30") == "j k l"
assert maioridade_penal("m n o p q r", "18 5 2 98 6 45") == "m p r"