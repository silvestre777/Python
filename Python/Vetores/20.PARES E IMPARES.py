import os

os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
pares= 0
impares =0
numeros = []

for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1} numero:"))
    numeros.append(numero)
    if numero % 2 == 0:
        pares+=1
    else:
        impares +=1

for i, numero in enumerate(numeros) :
    print(f"O {i+1}º numero é: {numero} ")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")