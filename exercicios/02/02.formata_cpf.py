cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

digito2 = cpf1 % 10
novo_cpf1 = cpf1 // 10
digito1 = novo_cpf1 % 10
novo_cpf1 = novo_cpf1 // 10
soma1 = digito2 + digito1

digito2_2 = cpf2 % 10
novo_cpf2 = cpf2 // 10
digito1_2 = novo_cpf2 % 10
novo_cpf2 = novo_cpf2 // 10
soma2 = digito2_2 + digito1_2

digito2_3 = cpf3 % 10
novo_cpf3 = cpf3 // 10
digito1_3 = novo_cpf3 % 10
novo_cpf3 = novo_cpf3 // 10
soma3 = digito2_3 + digito1_3

print(f"{novo_cpf1}-{digito1}{digito2}")
print(soma1)
print(f"{novo_cpf2}-{digito2_2}{digito2_2}")
print(soma2)
print(f"{novo_cpf3}-{digito2_3}{digito1_3}")
print(soma3)