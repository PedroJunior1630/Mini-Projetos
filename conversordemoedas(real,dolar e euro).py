real = float(input("Digite um valor em R$: "))

while True:
    print("=+=" * 15)
    print("""
    [1] Dolar
    [2] Euro
    [3] Novo valor
    [4] Encerrar o programa
    """)
    opcao = int(input("Digite sua opção: "))
    print("=+=" * 15)
    if opcao == 1:
        print(f"R${real:.2f} IGUAL A US${real / 5.32:.2f}")
    elif opcao == 2:
        print(f"R${real:.2f} IGUAL A EUROS {real / 5.53:.2f}")
    elif opcao == 3:
        real = float(input("Digite um valor em R$: "))
    if opcao == 4:
        break
print("PROGRAMA CONVERSÃO DE MOEDAS ENCERRADO...")
