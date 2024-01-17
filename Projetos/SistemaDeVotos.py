candidatos = ["Gustavo Guanabara 2013","Felipe Deschamps 2015","Lucas Montano 2017"]

def tempo():
    from time import sleep
    sleep(1.5)


def leiaInt(msg):
    while True:
        try:
            votando = int(input(msg))
        except:
            print("\033[31mERRO! VALOR INVÁLIDO.\033[m")
        else:
            return votando

        

def linha(tam=15,):
    print("=+=" * tam)

def cabecalho(msg):
    linha()
    print(msg.center(45))
    linha()
    tempo()

def verificaVoto(nome="Desconhecido",idade=0):
    if idade >= 18 and idade < 70:
        resultado =  "VOTO OBRIGATÓRIO"
    elif idade < 18:
        resultado = "NÃO VOTA"
    else:
        resultado = "VOTO OPCIONAL"
    return resultado


def votaCandidato():
    cabecalho("CANDIDATOS")
    for contador, pessoa in enumerate(candidatos):
        print(f"\033[33m{contador+1}° Candidato: \033[36m{pessoa}\033[m")
        tempo()
    print("\033[36m0 PARA NULO")
    print("OUTRO NÚMERO PARA EM BRANCO\033[m")
    linha()
    voto = leiaInt("VOTO: ")
    return voto


cabecalho("VOTAÇÃO")

nome = str(input('Nome: ')).title()
idade = int(input('Idade: '))
ficha = verificaVoto(nome,idade)

cabecalho(ficha)

if ficha == "VOTO OBRIGATÓRIO":
    candidatos = votaCandidato()
    cabecalho("FICHA DE VOTAÇÃO")
    tempo()
    print(f"{'NOME':.<20}{nome}")
    print(f"{'IDADE':.<20}{str(idade)} anos")
    print(f"{'VOTO':.<20}{str(candidatos)}")
    linha()
if ficha == "VOTO OPCIONAL":
    opc = str(input('Deseja votar?[S/N]: ')).strip().upper()
    if opc[0] == "S":
        candidatos = votaCandidato()
        cabecalho("FICHA DE VOTAÇÃO")
        tempo()
        print(f"{'NOME':.<20}{nome}")
        print(f"{'IDADE':.<20}{str(idade)} anos")
        print(f"{'VOTO':.<20}{str(candidatos)}")
        linha()
tempo()
cabecalho("PROGRAMA FINALIZADO...")
