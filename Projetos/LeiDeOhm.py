def tempo(seg):
    from time import sleep
    sleep(seg)
def linha(tam=20):
    print("=+=" * tam)

def cabecalho(msg):
    linha()
    print(msg.center(60))
    linha()

def layout(*item):
    cabecalho("QUE TIPO DE GRANDEZA DESEJA DESCOBRIR?")
    
def conversao(tipo):
    pass


cabecalho("CONVERSÃO DE GRANDEZAS ELÉTRICAS")
tempo(1)
layout("Tensão(Volts)", "Corrente(Amperes)","Resistência(Ohms)","Potência(Watts)")

