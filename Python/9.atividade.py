import os
os.system("cls || clear")

pares = 0
impares =0

for i in range (5):
    numero = int (input(f"Digite o {i+1} numero: "))

if numero % 2 ==0:
    pares = pares + numero
else:
    impares = impares + numero

print(f"Pares: {pares}")
print(f"Impares: {impares}")