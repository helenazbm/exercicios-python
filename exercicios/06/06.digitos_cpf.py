def calcula_digitos_verificacao(cpf):
    novo_cpf = ""
    resposta = ""

    i = 0
    soma = 0
    for n in range(10, 1, -1):
        soma += 10 * (int(n) * int(cpf[i]))
        digito_um = soma % 11

        if digito_um == 10:
            digito_um = 0

        novo_cpf = cpf + str(digito_um)
        i += 1

    indice = 0
    soma_dois = 0
    for x in range(11, 1, -1):
        soma_dois += 10 * (int(x) * int(novo_cpf[indice]))
        digito_dois = soma_dois % 11

        if digito_dois == 10:
            digito_dois = 0
    
        indice += 1

    resposta = str(digito_um) + str(digito_dois)

    return resposta

assert calcula_digitos_verificacao('153245875') == '40'
assert calcula_digitos_verificacao('085068754') == '39'
assert calcula_digitos_verificacao('840671444') == '15'