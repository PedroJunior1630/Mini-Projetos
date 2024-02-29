import os

def tempo(seg):
    from time import sleep
    sleep(seg)


def limpa():
    os.system("cls" if os.name == "nt" else "clear")


def linhaAnima():
    x = " "
    z =  x
    for l in range(0,10):
        print(z,"<__>")
        tempo(1)
        limpa()
        z = z + " "

def personagemAnima():
    for andar in range(0,60):
        print("""
             O
            /|>
            /|
        """)
        tempo(0.2)
        limpa()
        print("""
             O/
            /|
            /|
        """)
        tempo(0.2)
        limpa()
        print("""
             O
            <|>
            /|
        """)
        tempo(0.2)
        limpa()

personagemAnima()


print("""
   ________
 /         /|
/_________/ |
|         | |
|         | /
|_________|/
      
""")

print("""
_________
|        |
|        |
|________|

""")

