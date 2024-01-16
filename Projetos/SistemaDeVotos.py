candidatos = {"nome":'Gustavo Guanabara',
              'Felipe Deschamps',
              'Alfredo',
              'Lira'
              }

def linha(tam=10):
    print("=+=" * tam)

def cabecalho(msg):
    linha()
    print(msg.center(30))
    linha()

def verificaIdade(idade):
    if idade >= 18 and idade < 70:
        return "VOTO OBRIGATÓRIO";
    elif idade < 18:
        return "NÃO VOTA";
    else:
        return "VOTO NÃO OBRIGATÓRIO";
def votaCandidato():
    cabecalho("CANDIDATOS")
    for contador, pessoa in enumerate(candidatos):
        print(f"{contador+1}° Candidato: {pessoa}")

cabecalho("VOTAÇÃO")
idade = verificaIdade(int(input('Digite sua idade:')))
if idade == "VOTO OBRIGATÓRIO":
    candidatos = votaCandidato()
