import os
"""
form dataclasses import dataclass   
#Constante
QUANTIDADE_ALUNOS = 2


@dataclass
class Aluno:
    nome: str
    idade: int

alunos = []

#Solicitando dados ao usuario.

for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome: ")
    idade_do_aluno = int(input("Digite sua idade: "))

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno)
    alunos.append(aluno)

    # Exibindo dados para o usuario

for aluno in alunos:
    print(f"Nome: {aluno.nome_do_aluno}")
    print(f"Idade: {aluno.idade_do_aluno}")


"""


#constante
QUANTIDADE_ALUNO= 2

nomes = []
idades = []
os.system("cls || clear")
#Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNO):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite a idade: "))
    nomes.append(nome)
    idades.append(idade)
os.system("cls || clear")
#Exibindo dados para o usuário.
for i in range (QUANTIDADE_ALUNO):
    print(f"{i+1}º Nome: {nomes[i]}")
    print(f"{i+1}º Idade: {idades[i]}")