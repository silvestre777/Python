import os

os.system ("cls || clear")

while True:
    print("==== Menu ====")
    print("1- Picanha - R$ 25,00")
    print("2- Lasanha - R$ 20,00")
    print("3- Strogonoff - R$ 18,00")
    print("4- Bife Acebolado - R$ 15,00")
    print("5- Pão com ovo - R$ 5,00")
    op = int (input("Digite a opção: "))

        
    match(op):
        case 1:
            print("1- Picanha - R$ 25,00")
            break
        case 2:
            print("2- Lasanha - R$ 20,00")
            break
        case 3:
            print("3- Strogonoff - R$ 18,00")
            break
        case 4:
            print("4- Bife Acebolado - R$ 15,00")
            break
        case 5:
            print("5- Pão com ovo - R$ 5,00")
            break
        case _:
            input("Opção invalida")
            os.system ("cls || clear")