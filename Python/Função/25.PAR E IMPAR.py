import os


def verificar_par(numeros):
    pares =0
    for numero in numeros:
        if numero % 2 ==0:
            pares +=1
    return pares
def verificar_impar (numeros):
    impares=0
    for numero in numeros:
        if numero % 2 !=0:
            impares+=1
    return impares
    

lista_numeros =[]
QUANTIDADE_NUMEROS = 2
for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o numero: "))
    lista_numeros.append(numero)

quantidade_pares = verificar_par(lista_numeros)
quantidade_impares = verificar_impar(lista_numeros)

print(f"Quantidade pares: {verificar_par(quantidade_pares)}")
print(f"Quantidade impares: {verificar_impar(quantidade_impares)}")