def linha():
    print("=-=" * 20)

linha()
print("FATORIAL")
linha()


def fatorial(n1,n2=0):
    if n2 != 0:
        f1 = 1
        print(f"{n1}! = ",end = "")
        for c in range(n1,0,-1):
            f1 = f1 * c
            print(f"{c}",end = "")
            print(" x " if c > 1 else " = ",end = "")
        print(f"{f1}")

        f2 = 1
        print(f"{n2}! = ",end = "")
        for c in range(n2,0,-1):
            f2 = f2 * c
            print(f"{c}",end = "")
            print(" x " if c > 1 else " = ",end = "")
        print(f"{f2}")

        div = f1 / f2

        print(f"{f1} / {f2} =  {div:.2f}")
    else:
        f = 1
        print(f"{n1}! = ",end = "")
        for c in range(n1,0,-1):
            f = f * c
            print(f"{c}",end = "")
            print(" x " if c > 1 else " = ",end = "")
        print(f"{f}")

while True:
    
    d = str(input("Vai dividir fatoriais?[S/N]: ")).upper()
    if d == "S":
        linha()
        n1 =  int(input("Digite o 1° número fatorial: "))
        n2 =  int(input("Digite o 2° número fatorial: "))
        fatorial(n1,n2)
    else:
        linha()
        n =  int(input("Digite um número fatorial: "))
        fatorial(n)
    linha()
    opc = str(input('Deseja continuar[S/N]? ')).upper()
    if opc[0] == "N":
        break
