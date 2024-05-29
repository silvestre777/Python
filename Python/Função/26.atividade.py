import os

os.system("cls || clear")

resultado = False

while True:

    a = int(input("Digite o primeiro numero: "))
    operador = input("Digite o operador: + - * /: ")
    b= int(input("Digite o segundo numero: "))

    match(operador):
        case '+':
            resultado = a+b
            break
        case '-':
            resultado = a-b
            break
        case '*':
            resultado = a*b
            break
        case '/':
            resultado = a/b
            break
        case _:
            print("Opção invalida")

print(f"Resultado: {resultado}")