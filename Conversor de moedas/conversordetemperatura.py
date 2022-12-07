graus = float(input("Digite a temperatura: "))
print("=+=" * 20)
print("""Escolha a temperatura 
| [1] Graus C° | | [2] Graus F° | | [3] Graus K° |  
""")
temperatura = int(input("Qual sua opção: "))
while True:
    print("=+=" * 20)
    print("""Escolha a temperatura para conversão
    [1] Graus C°
    [2] Graus F°
    [3] Graus K°
    [4] Encerrar o programa
    [5] Nova temperatura
    """)
    opcao = int(input("Digite sua opção de conversão: "))

    if opcao == 4:
        break
    if temperatura == 1:
        if opcao == 2:
            print(f"{graus} C° IGUAL A  {graus  * 9 / 5 + 32} F°")
        if opcao == 3:
            print(f"{graus} C° IGUAL A {graus + 273.15 } K°")

    if temperatura == 2:
        if opcao == 1:
            print(f"{graus} F° IGUAL A {(graus - 32) * 5 / 9:.2f} C°")
        if opcao == 3:
            print(f"{graus} F° IGUAL A {(graus - 32) * 5 / 9 + 273.15:.2f} K°")

    if temperatura == 3:
        if opcao == 1:
            print(f"{graus} K° IGUAL A {graus - 273.15} C°")
        if opcao == 2:
            print(f"{graus} K° IGUAL A {(graus - 273.15) * 9 / 5 + 32} F°")

    if opcao == 5:
        graus = float(input("Digite a temperatura: "))
        print("=+=" * 20)
        print("""Escolha a temperatura 
        | [1] Graus C° | | [2] Graus F° | | [3] Graus K° |  
        """)
        temperatura = int(input("Qual sua opção: "))
print("PROGRAMA ENCERRADO COM SUCESSO!")
