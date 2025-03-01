area = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = (area * aliquota) + 35

print(f"IPTU: R$ {iptu:.2f}")

print()
print("Pagamento:")

quota = iptu * 0.75
desconto_seis = iptu * 0.95
parcela_seis = desconto_seis / 6
parcela_dez = iptu / 10

print(f"1. Quota única. R$ {quota:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {desconto_seis:.2f}")
print(f"   6 x R$ {parcela_seis:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {iptu:.2f}")
print(f"   10 x R$ {parcela_dez:.2f}")