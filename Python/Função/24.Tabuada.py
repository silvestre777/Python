import os

def logoSenai():
    os.system("cls || clear")
    print("=================")
    print(f"=======SENAI=======")
    print(f"================")

def multiplica(n1,i):
    return n1 * i
logoSenai()
numero = int(input(f"Digite o numero que deseja a tabuada: "))
for i in range (1,11):
    print(f"{numero} x {i} = {multiplica(numero,i)}")