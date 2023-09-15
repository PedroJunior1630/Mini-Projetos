print("=+=" * 20)
print("         IMPOSTO DE RENDA")
print("=+=" * 20)
tipo = 0
salario = float(input('Digite a sua renda mensal: R$ '))
print("\n")
print("=-=" * 20)
print("TABELA DE IMPOSTO DE RENDA(IRPF)")
print("""
ATÉ R$2.112,00 > 0%
DE R$2.112,00 - R$2.826.65 > 7,5%
DE R$2.826.65 - R$3.571,05 > 15,0%
DE R$3.571,05 - R$4.664,68 > 22,5%
ACIMA DE R$4.664,68 > 27,5%
""")
print("=-=" * 20)
print("\n")
if salario <= 2112:
    irpf = 0
    tipo = 0
elif salario > 2112 and salario <= 2826.65:
    irpf = salario * 7.5 / 100
    tipo = 7.5
elif salario > 2826.65 and salario <= 3571.05:
    irpf = salario * 15 / 100
    tipo = 15
elif salario > 3571.05 and salario <= 4664.68:
    irpf = salario * 22.5 / 100
    tipo = 22.5
else:
    irpf = salario * 27.5 / 100
    tipo = 27.5
print(f"Com renda mensal de R${salario:.2f} seu imposto de renda é de {tipo:.2f}% sobre a renda.")
print(f'Imposto de renda: R${irpf:.2f}')
print("\n")
