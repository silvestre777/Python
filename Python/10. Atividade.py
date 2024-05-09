import os
os.system("cls || clear")

media =0
soma = 0
contador = 0
for i in range (4):
    nota = float (input(f"Digite a {i+1} nota:"))
    soma +=nota
    contador = contador +1

media = soma/contador

print(f"Media: {media}")



