import os
os.system("cls || clear")

nota = -1


while (nota < 0 or nota > 10):
    nota = float (input("Digite a nota:"))

print(f"Nota: {nota}")