import os
def logoSenai():
    os.system("cls || clear")
    print("=================")
    print(f"=======SENAI=======")
    print(f"================")


def somar(n1,n2):
    resultado = n1+n2
    return resultado
def multiplicar(n1,n2):
    resultado = n1*n2
    return resultado
def subtracao(n1,n2):
    resultado = n1-n2
    return resultado
def dividir (n1,n2):
    resultado = n1/n2
    return resultado

logoSenai()
primeiroNumero = int(input("Digite o primeiro numero: "))

logoSenai()
segundoNumero=int(input("Digite o segundo numero: "))

logoSenai()
soma = somar(primeiroNumero, segundoNumero)
subtrair = subtracao (primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero,segundoNumero)
divisao = dividir (primeiroNumero, segundoNumero)


print(f"Soma: {soma}")
print(f"Subtração: {subtrair}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


