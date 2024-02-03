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

def conversao(tipo):
    


cabecalho("CONVERSÃO DE GRANDEZAS ELÉTRICAS")
tempo(1)
interface = layout("Tensão[Volts]", "Corrente[Amperes]","Resistência[Ohms]","Potência[Watts]")
if interface == 0:
    print("\033[1;97m...")
    tempo(1)
    cabecalho(" Programa Finalizado.")
else:
    conversao(interface)
