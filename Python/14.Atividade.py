import os

os.system("cls || clear")
soma= 0
contador = 0
media = 0

numero = 1
# numero = int (input("Digite um numero positivo: "))

while numero >0:
    contador = contador +1
    numero = int (input("Digite um numero positivo: "))
    soma += numero

media = soma / contador

print(f"Media: {media}")
