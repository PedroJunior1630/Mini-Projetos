contador = abaixo = normal = acima = obeso = morbida =  maior = menor = maior_altura = menor_altura = 0
imc = pessoa = 1
opcao = "S"

print("\033[1;32m=+=" * 20)
print("LEITOR DE PESO,ALTURA E CALCULADOR DE IMC")
print("=+=" * 20)

while opcao[0] == "S": 

    print(f"\033[1;36m{pessoa}° Pessoa digite seu peso em KG e sua altura em M")

    pessoa = pessoa + 1
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura(M): "))
    
    print("=+=" * 20)
    opcao = str(input("\033[1;97mDeseja continuar com mais pessoas?[S/N] ")).strip().upper()[0]
    print("=+=" * 20)

    imc = peso / (altura * altura)
    contador = contador + 1

    if imc <18.5:
        abaixo = abaixo + 1
    if imc > 18.5 and imc < 25:
        normal = normal + 1
    if imc >= 25 and imc < 30:
        acima = acima + 1
    if imc >= 30 and imc < 40:
        obeso = obeso + 1
    if imc >= 40:
        morbida = morbida + 1

    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    if contador == 1:
        maior_altura = altura
        menor_altura = altura
    else:
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura
            
print("\033[1;97m=+=" * 20)

print(f"\033[1;35mO maior peso registrado foi {maior}Kg \nO menor peso registrado foi {menor} Kg")

print("\033[1;97m=+=" * 20)

print(f"\033[1;35mA maior altura registrada foi {maior_altura}M \nA menor altura registrada foi {menor_altura}M ")

print("\033[1;97m=+=" * 20)

print(f"\033[1;33m{abaixo} pessoas abaixo do peso")
print(f"\033[1;32m{normal} pessoas com peso normal \n{acima} pessoas acima do peso")
print(f"\033[1;31m{obeso} pessoas com obesidade \n{morbida} pessoas com obesidade morbida")

print("\033[1;97m=+=" * 20)
