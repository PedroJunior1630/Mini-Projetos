print("=+=" * 20)
print("CONVERSOR DE DADOS - BASE")
print(""" 
    - BYTE [1]
    - KILOBYTE [2]
    - MEGABYTE [3]
    - GIGABYTE [4]
    - TERABYTE [5]
""")
print("=+=" * 20)

#listas
lista = ['n.da','BYTE(s)','KILOBYTE(s)','MEGABYTE(s)','GIGABYTE(s)','TERABYTE(s)']
lista_abreviada = ['n.da','BY','KB','MB','GB','TB']

#inputs
opcao = int(input('Digite qual base deseja converter: '))
valor = int(input('Digite o valor: '))
conversao = int(input('Digite a outra base: '))
print("\n")

print(f"CONVERSÃO DE {lista[opcao]} PARA {lista[conversao]}")
print("\n")

if opcao == 1:

    if conversao == 2:
        x = valor / 1000

    if conversao == 3:
        x = valor * 10 ** -6

    if conversao == 4:
        x = valor * 10 ** -9

    if conversao == 5:
        x = valor * 10 ** -12

elif opcao == 2:

    if conversao == 1:
        x = valor * 1000

    if conversao == 3:
        x = valor / 1000

    if conversao == 4:
        x = valor * 10 ** -6

    if conversao == 5:
        x = valor * 10 ** -9

elif opcao == 3:

    if conversao == 1:
        x = valor * 10 ** -6

    if conversao == 2:
        x = valor * 1000

    if conversao == 4:
        x = valor / 1000

    if conversao == 5:
        x = valor * 10 ** -6

elif opcao == 4:

    if conversao == 1:
        x = valor * 10 ** 9

    if conversao == 2:
        x = valor * 10 ** 6

    if conversao == 3:
        x = valor * 1000

    if conversao == 5:
        x = valor / 1000

elif opcao == 5:

    if conversao == 1:
        x = valor * 10 ** 12
    if conversao == 2:
        x = valor * 10 ** 9
    if conversao == 3:
        x = valor * 10 ** 6
    if conversao == 4:
        x = valor * 1000

print(f'{valor} {lista_abreviada[opcao]} equivalem a: {x} {lista_abreviada[conversao]}')
