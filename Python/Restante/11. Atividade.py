import os
os.system("cls || clear")

media =0
soma = 0
contador = 0
for i in range (3):
    nota = float (input(f"Digite a {i+1} nota:"))
    soma +=nota
    contador = contador +1

media = soma/contador

print(f"Media: {media}")

if media >= 7:
    print(f"Aprovado")
elif media >=4:
    print(f"Recuperação")
else:
    print(f"Reprovado")
