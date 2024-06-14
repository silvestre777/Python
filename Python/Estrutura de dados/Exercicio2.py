import os

os.system("cls || clear")
from dataclasses import dataclass
pet = []
QUANTIDADE_PETS = 2
@dataclass
class Pet:
    def __init__(self, nome: str, idade: int, raca, porte, alimentacao):
        self.nome= nome
        self.idade = idade
        self.raca= raca
        self.porte = porte
        self.alimentacao= alimentacao

os.system("cls || clear")
for i in range(QUANTIDADE_PETS):
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    raca = input("Digite a raça do animal: ")
    porte = input ("Digite o porte do animal 'Pequeno', 'Medio', 'Grande': ")
    alimentacao = input("Digite o tipo de alimentação do animal: ")
    pet.append(Pet(nome,idade,raca,porte,alimentacao))

for i in pet:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Raça: {i.raca}")
    print(f"Porte do animal: {i.porte}")
    print(f"Tipo de alimentação: {i.alimentacao}")
    print("\n")