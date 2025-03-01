reprovados = 0
while True:
    seq = input()
    if seq == "-":
        break

    i = 0 
    falta = 0
    while i < len(seq):
        if seq[i] == "f":
            falta += 1
        i += 1

    if falta > 8:
        reprovados += 1

print(f"{reprovados} aluno(s) reprovado(s) por falta.")