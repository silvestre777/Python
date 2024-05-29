import os

os.system ("cls || clear")

while True:
    numero = int(input("Digite um numero de 1 a 7: "))

    match(numero):
        case 1:
            print("Domingou com Jesus \n Dia descansar")
            break
        case 2:
            print("Segunda abençoada, dia de trabalhar \n Dia util")
            break
        case 3:
            print("Terçou com a benção de Deus \n Dia util toda vida")
            break
        case 4:
            print("Quarta abençoada \n Dia util")
            break
        case 5:
            print("Quinta abençoada com certeza \n Dia util")
            break
        case 6:
            print("Sextou com Jesus, sem ele nem tente \n Dia util")
            break
        case 7:
            print("Sabadou da melhor forma, trabalhando, dia de descanso logo apos")
            break
        case _:
            input("Opção invalida")
