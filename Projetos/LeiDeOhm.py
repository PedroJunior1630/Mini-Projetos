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


def grandeza(msg,tipo=""):
    cabecalho(msg)
    print("QUAIS VALORES VOCÊ POSSUI?")
    print("\033[1;34m")

    if tipo == "volts":
        valores = [input("Amperagem?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Potência?[S/N]").upper()]
    elif tipo == "amperes":
        valores = [input("Volts?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Potência?[S/N]").upper()]
    elif tipo == "resistencia":
        valores = [input("Amperagem?[S/N]").upper(),input("Volts?[S/N]").upper(),input("Potência?[S/N]").upper()]
    elif tipo == "potencia":
        valores = [input("Amperagem?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Volts?[S/N]").upper()]

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
        valor = grandeza("TENSÃO ELÉTRICA(VOLTS)","volts")
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
            print("V = √P x A")
            tempo(0.5)
            print(f"V = √{po} x {re}")
            tempo(0.5)
            print(f"V = √{po*re}")
            tempo(0.5)
            print(f"V = {(po*re)**(1/2):.2f}")
            linha()

    elif tipo == 2:
        valor = grandeza("CORRENTE ELÉTRICA(AMPERES)","amperes")
        linha()
        if valor[0] == "S" and valor[1] == "S":
            vo = pergunta("Volts")
            re = pergunta("Ohms")
            formula("A","V","/","R",vo,re)
        elif valor[0] == "S" and valor[2] == "S":
            po = pergunta("Watts")
            vo = pergunta("Volts")
            formula("A","P","/","V",po,vo)
        elif valor[1] == "S" and valor[2] == "S":
            re = pergunta("Ohms")
            po = pergunta("Watts")
            linha()
            print("I = √P / R")
            tempo(0.5)
            print(f"V = √{po} / {re}")
            tempo(0.5)
            print(f"V = √{po/re:.2f}")
            tempo(0.5)
            print(f"V = {(po/re)**(1/2):.2f}")
            linha()
    elif tipo == 3:
        valor = grandeza("RESISTÊNCIA(OHMS)","resistencia")
        if valor[0] == "S" and valor[1] == "S":
            am = pergunta("Amperes")
            vo = pergunta("Volts")
            formula("R","V","/","A",vo,am)
        elif valor[0] == "S" and valor[2] == "S":
            am = pergunta("Amperes")
            po = pergunta("Watts")
            linha()
            print("R = P / A²")
            tempo(0.5)
            print(f"R = {po} / {am}²")
            tempo(0.5)
            print(f"R = {po} / {am**2}")
            tempo(0.5)
            print(f"R = {po/am:.2f}")
            linha()
        elif valor[1] == "S" and valor[2] == "S":
            vo = pergunta("Volts")
            po = pergunta("Watts")
            linha()
            print("R = V² / P")
            tempo(0.5)
            print(f"R = {vo}² / {po}")
            tempo(0.5)
            print(f"R = {vo**2} / {po}")
            tempo(0.5)
            print(f"R = {vo/po:.2f}")
            linha()
    elif tipo == 4:
        valor = grandeza("POTÊNCIA ELÉTRICA(WATTS)","potencia")
        if valor[0] == "S" and valor[1] == "S":
            am = pergunta("Amperes")
            re = pergunta("Ohms")
            linha()
            print("P = R x A²")
            tempo(0.5)
            print(f"P = {re} x {am}²")
            tempo(0.5)
            print(f"P = {re} x {am**2}")
            tempo(0.5)
            print(f"P = {re*am}")
            linha()
        if valor[0] == "S" and valor[2] == "S":
            vo = pergunta("Volts")
            am = pergunta("Amperes")
            formula("P","V","x","A",vo,am)
        if valor[1] == "S" and valor[2] == "S":
            vo = pergunta("Volts")
            re = pergunta("Ohms")
            linha()
            print("P = V² / R")
            tempo(0.5)
            print(f"P = {vo}² / {re}")
            tempo(0.5)
            print(f"P = {vo**2} / {re}")
            tempo(0.5)
            print(f"P = {vo**2 / re}")
            linha()
cabecalho("CONVERSÃO DE GRANDEZAS ELÉTRICAS")
tempo(1)
interface = layout("Tensão[Volts]", "Corrente[Amperes]","Resistência[Ohms]","Potência[Watts]")
if interface == 0:
    print("\033[1;97m...")
    tempo(1)
    cabecalho(" Programa Finalizado.")
else:
    conversao(interface)
