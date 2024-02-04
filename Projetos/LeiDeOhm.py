AZUL = "\033[1;36m"

def tempo(seg):
    from time import sleep
    sleep(seg)


def linha(tam=20):
    print(AZUL)
    print("=+=" * tam)
    print("\033[m")

def cabecalho(msg):
    print("\033[1;33m")
    linha()
    print(f"\033[1;33m {msg.center(60)}\033[m")
    linha()
    print("\033[m")


def leiaInt(inp):
    while True:
        try:
            a =  int(input(inp))
        except:
            print("\033[31mERRO! DIGITE UM NÚMERO INTEIRO OU DE ACORDO COM A TABELA!\033[m")
        else:
            if a > 4 or a < 0:
                continue
            else:
                return a


def layout(*item):
    cabecalho("QUE TIPO DE GRANDEZA DESEJA DESCOBRIR?")
    print("\033[1;16m")
    for num, grandeza in enumerate(item):
        print(f"[ {num+1} ] - {grandeza:<15}")
    print(f"[ 0 ] - Para finalizar.")
    print("\033[m")
    opc = leiaInt('\033[1;97mQual opção Deseja?\033[m')
    return opc

def pergunta(tipo):
    v = int(input(f"\033[1;33mQuantos {tipo}? \033[m"))
    return v


def grandeza(msg):
    cabecalho(msg)
    print("QUAIS VALORES VOCÊ POSSUI?")
    print("\033[1;34m")
    valores = [input("Amperagem?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Potência?[S/N]").upper()]
    print("\033[m")
    return valores

def formula(*valores):
    linha()
    print(f"{valores[0]} = {valores[1]} {valores[2]} {valores[3]}")
    tempo(0.5)
    print(f"{valores[0]} = {valores[-2]} {valores[2]} {valores[-1]}")
    tempo(0.5)
    if valores[2] == "/":
        print(f"{valores[0]} = {valores[-2] / valores[-1]:.2f}")
    elif valores[2] == "x":
        print(f"{valores[0]} = {valores[-2] * valores[-1]:.2f}")
    linha()


def conversao(tipo):
    if tipo == 1:
        valor = grandeza("TENSÃO ELÉTRICA(VOLTS)")
        linha()
        if valor[0] == "S" and valor[2] == "S":
            wa = pergunta("Watts")
            am = pergunta("Amperes")
            formula("V","P","/","A",wa,am)

        elif valor[0] == "S" and valor[1] == "S":
            am = pergunta("Amperes")
            re = pergunta("Ohms")
            formula("V","R","x","A",am,re)

        elif valor[1] == "S"  and valor[2] == "S":
            re = pergunta("Ohms")
            po = pergunta("Watts")
            linha()
            print("V = P / A")
            tempo(0.5)
            print(f"V = √{po} x {re}")
            tempo(0.5)
            print(f"V = √{po*re}")
            tempo(0.5)
            print(f"V = {(po*re)**(1/2):.2f}")
            linha()

    elif tipo == 2:
        valor = grandeza("CORRENTE ELÉTRICA(AMPERES)")
        linha()
        if valor[0] == "S" and valor[1] == "S":

        elif valor[0] == "S" and valor[2] == "S":

        elif valor[1] == "S" and valor[2] == "S":
            
cabecalho("CONVERSÃO DE GRANDEZAS ELÉTRICAS")
tempo(1)
interface = layout("Tensão[Volts]", "Corrente[Amperes]","Resistência[Ohms]","Potência[Watts]")
if interface == 0:
    print("\033[1;97m...")
    tempo(1)
    cabecalho(" Programa Finalizado.")
else:
    conversao(interface)
