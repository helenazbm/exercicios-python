#atividade - unidade 03
#maria helena barros
#controle de qualidade

congelado = float(input())
descongelado = float(input())

porcentagem = ((congelado - descongelado) * 100) / congelado 

qualidade = ""

if porcentagem >= 5 and porcentagem <= 10:
    qualidade = "Produto em conformidade."

elif porcentagem < 5:
    qualidade = "Produto qualis A."

else: 
    qualidade = "Produto não conforme."

print(f"{porcentagem:.1f}% do peso do produto é de água congelada.")
print(qualidade)