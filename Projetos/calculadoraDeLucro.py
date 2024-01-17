produtos = []
produto = {}
total = 0
def tempo(d=0.8):
    from time import sleep
    sleep(d)


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except:
            print("\033[31mERRO! DIGITE UM VALOR NUMÉRICO\033[m")
        else:
            return a


def linha(tam=20):
    print("=+=" * tam)


def cabecalho(msg):
    linha()
    print(msg.center(60))
    linha()
    tempo()


def moeda(coin):
    while True:
        a = input(coin)
        if a.isnumeric():
            return float(a)
        else:
            t = a.replace(',','.')
            if t.isalnum():
                print("\033[31mERRO! DIGITE UM VALOR VÁLIDO!\033[m")
            else:
                return float(t)


cabecalho("PRODUTO")
produtonome = str(input('Qual nome do produto? '))
fabrica = leiaInt(f'Quantos {produtonome}(s) pretende fabricar?')
qntd = leiaInt('Quantos ingredientes são necessários? ')
linha()
tempo()

for c in range(0,qntd):
    cabecalho(f"{c+1}° PRODUTO")
    produto["nome"] = str(input(f'Nome do {c+1}° ingrediente: '))
    produto["preço"] = moeda(f'Preço do {produto["nome"]} R$')
    produto["quantidade"] = leiaInt('Quantidade: ')
    produtos.append(produto.copy())
    produto.clear()
linha()
tempo()

cabecalho(f"{produtonome}") 
for valor in produtos:
    preco = valor["quantidade"] * valor["preço"]
    total += preco
    print(f'{valor["nome"]:.<30}R${preco:>5.2f}')
    tempo(0.5)
print(f'{"Total:":.<30} R${total:>5.2f}')
#custo por produto
cabecalho("CUSTO POR PRODUTO")
print(f"R${total/fabrica:.2f}")

