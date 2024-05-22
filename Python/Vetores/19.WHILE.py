import os
import sys
QUANTIDADE_NUMEROS = 5
numeros = []
maiorNumero=0
menorNumero=sys.maxsize
os.system("cls || clear")
while numero >0:
        numero = float(input(f"Digite o {i+1} numero:"))
    if numero == 0:
        numeros.append(numero)
        break
 maiorNumero = max(numero,maiorNumero)
menorNumero = min(numero,menorNumero)
for i, numero in enumerate(numeros):
    print(f"{i+1}º Numero: {numero}")

print(f"O menor numero é: {menorNumero}")
print(f"O maior numero é: {maiorNumero}")