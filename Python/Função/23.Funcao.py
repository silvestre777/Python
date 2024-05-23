import os
QUANTIDADE_NUMERO = 5

def logoSenai():
    os.system("cls || clear")
    print("=================")
    print(f"=======SENAI=======")
    print(f"================")

def calcMedia (soma,QUANTIDADE_NUMERO):
    return soma / QUANTIDADE_NUMERO

soma = 0
for i in range (QUANTIDADE_NUMERO):
    logoSenai()
    numero = int(input(f"Digite o {i+1} numero: "))
    soma +=numero
media = calcMedia(soma,QUANTIDADE_NUMERO)

logoSenai()
print(f"Media: {media}")