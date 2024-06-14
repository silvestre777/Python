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
    os.system("cls || clear")
    aluno= Aluno(
        nome = input("Digite seu nome: "),
        idade = input("Digite sua idade: "),
        sexo = input("Digite seu sexo 'F' ou 'M': ").upper(),
        telefone =input("Digite seu telefone: "),
        altura = input("Digite sua altura: "),
        peso =input("Digite seu peso: ")

       #o.upper()
    )
    alunos.append(aluno)

    # Exibindo dados para o usuario

os.system("cls || clear")
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Sexo: {i.sexo}")
    print(f"Telefone: {i.telefone}")
    print(f"Altura: {i.altura}")
    print(f"Peso: {i.peso}")
    print("\n")