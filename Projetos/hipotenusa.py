import time
def tempo(seg):
    time.sleep(seg)
def desenhoPitagoras(valor):
    if valor == 'h':
        print(f'h² = {ca}² + {co}²')
        tempo(1)
        print(f'h² = {ca**2} + {co**2}')
        tempo(1)
        print(f'h² = {ca**2 + co**2}')
        tempo(1)
        print(f'h = √{ca**2 + co**2}')
        tempo(1)
        print(f'h = {(ca**2+co**2)**(1/2):.2f}')
    if valor == 'ca':
        print(f'{h}² = ca² + {co}²')
        tempo(1)
        print(f'{h**2} = ca² + {co**2}')
        tempo(1)
        print(f'ca² = {h**2} - {co**2}')
        tempo(1)
        print(f'ca = √{h**2 - co**2}')
        tempo(1)
        print(f'ca = {(h**2 - co**2) ** (1/2):.2f}')
    if valor == 'co':
        print(f'{h}² = co² + {ca}²')
        tempo(1)
        print(f'{h**2} = co² + {ca**2}')
        tempo(1)
        print(f'co² = {h**2} - {ca**2}')
        tempo(1)
        print(f'co = √{h**2 - ca**2}')
        tempo(1)
        print(f'co = {(h**2 - ca**2) ** (1/2):.2f}')
    print("\n")
print("=+=" * 20)
print("TEOREMA DE PITÁGORAS")
print("---" * 10)
print('Digite "0" para os valores que você não sabe.')
print("=+=" * 20)

#formula
# h² = ca² + co²

co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
h = float(input("Hipotenusa: "))
print("\n")

if ca != 0 and co != 0 and h == 0:
    x = (ca**2 + co**2)**(1/2)
    desenhoPitagoras('h')
    print(f"Hipotenusa: {x:.2f}")

elif ca != 0 and co == 0 and h != 0:
    x = (h**2 - ca**2)**(1/2)
    desenhoPitagoras('co')
    print(f"Cateto Oposto: {x:.2f}")

elif ca == 0 and co != 0 and h != 0:
    x = (h**2 - co**2) ** (1/2)
    desenhoPitagoras('ca')
    print(f"Cateto Adjacente: {x:.2f}")

print("\n")
