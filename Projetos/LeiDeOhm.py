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


def conversao(tipo):
    if tipo == 1:
        cabecalho("TENSÃO ELÉTRICA(VOLTS)")
        print("QUAIS VALORES VOCÊ POSSUI?")
        print("\033[1;34m")
        valores = [input("Amperagem?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Potência?[S/N]").upper()]
        print("\033[m")
        
        linha()
        if valores[0] == "S" and valores[2] == "S":
            wa = pergunta("Watts")
            am = pergunta("Amperes")
            linha()
            print("V = P / A")
            tempo(0.5)
            print(f"V = {wa} / {am}")
            tempo(0.5)
            print(f"V = {wa/am:.2f}")
            linha()

        elif valores[0] == "S" and valores[1] == "S":
            am = pergunta("Amperes")
            re = pergunta("Ohms")
            linha()
            print("V = R * A")
            tempo(0.5)
            print(f"V = {am} x {re}")
            tempo(0.5)
            print(f"V = {am*re:.2f}")
            linha()

        elif valores[1] == "S"  and valores[2] == "S":
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


cabecalho("CONVERSÃO DE GRANDEZAS ELÉTRICAS")
tempo(1)
interface = layout("Tensão[Volts]", "Corrente[Amperes]","Resistência[Ohms]","Potência[Watts]")
if interface == 0:
    print("\033[1;97m...")
    tempo(1)
    cabecalho(" Programa Finalizado.")
else:
    conversao(interface)
