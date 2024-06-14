from dataclasses import dataclass
import os


os.system("cls || clear")
#Constante
QUANTIDADE_ALUNOS = 2


@dataclass
class Aluno:
    nome: str
    idade: int
    sexo: str
    telefone: int
    peso: float
    altura: float

alunos = []

#Solicitando dados ao usuario.

for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome: ")
    idade_do_aluno = input("Digite sua idade: ")
    sexo_do_aluno = input("Digite seu sexo 'F' ou 'M': ")
    telefone_do_aluno =input("Digite seu telefone: ")
    altura_do_aluno = input("Digite sua altura")
    peso_do_aluno =input("Digite seu peso: ")

    os.system("cls || clear")
    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno, sexo = sexo_do_aluno, telefone= telefone_do_aluno)
    alunos.append(aluno)
    sexo_do_aluno.upper()

    # Exibindo dados para o usuario

os.system("cls || clear")
for i in alunos:
    print(f"Usuario {i+1}: ")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Sexo: {i.sexo}")
    print(f"Telefone: {i.telefone}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")
    print("\n")
