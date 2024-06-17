import os
from dataclasses import dataclass 

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

@dataclass
class Dados:
  
    nome: str
    sobrenome: str  
    idade: int
    altura: float
    peso: float
    resultado: str
    imc: float 

def calcular_imc(peso, altura):
    imc = peso / (altura *altura)
    return imc

def resultado_imc(imc):
    if imc <  18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"
    return resultado

dados = [] 

while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
   
    imc = calcular_imc(peso, altura)

    resultado = resultado_imc(imc)
    
    dadosUsuario = Dados(nome = nome, sobrenome = sobrenome, idade = idade, altura = altura, peso = peso, imc = imc, resultado = resultado)
    dados.append(dadosUsuario)
    
    

logoSenai()
print("\nDados dos usuarios: \n")
for i in dados:
    print(f"Nome completo: {i.nome} {i.sobrenome}")
    print(f"Idade: {i.idade}")
    print(f"Altura: {i.altura:.2f}")
    print(f"Peso: {i.peso:.2f}","kg")
    print(f"IMC: {i.imc:.2f}")
    print(f"Classificação: {i.resultado}")
 