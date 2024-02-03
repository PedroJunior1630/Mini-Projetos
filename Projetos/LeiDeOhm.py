def tempo(seg):
    from time import sleep
    sleep(seg)


def linha(tam=20):
    print("=+=" * tam)


def cabecalho(msg):
    linha()
    print(msg.center(60))
    linha()


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
    for num, grandeza in enumerate(item):
        print(f"[ {num+1} ] - {grandeza:<15}")
    print(f"[ 0 ] - Para finalizar.")
    opc = leiaInt('Qual opção Deseja?')
    return opc

def pergunta(tipo):
    v = int(input(f"Quantos {tipo}? "))
    return v


def conversao(tipo):
    if tipo == 1:
        cabecalho("TENSÃO ELÉTRICA(VOLTS)")
        print("QUAIS VALORES VOCÊ POSSUI?")
        valores = [input("Amperagem?[S/N]").upper(),input("Resistência?[S/N]").upper(),input("Potência?[S/N]").upper()]
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
