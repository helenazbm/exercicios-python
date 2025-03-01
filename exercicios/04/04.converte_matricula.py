antiga = input()
nova_matricula = ""


nova_matricula += "1"

for x in range(1, 5):
    nova_matricula += antiga[x]

nova_matricula += "0"

for i in range(5, 8):
    nova_matricula += antiga[i]


print(nova_matricula)