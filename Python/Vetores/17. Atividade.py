import os

os.system("cls || clear")

notas = []
soma = 0
media = 0
for i in range (3):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)
    soma = soma + nota
media = soma /3

for i in range(3):
    print(f"A nota  é igual: {notas[i]}")

print (f"A media é: {media}")


""""

Forma 6

# Exemplo 6
for nota in notas:
    print(f"Nota: {notas[i]}")
"""