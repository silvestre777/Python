import os
from dataclasses import dataclass

os.system("cls || clear")
@dataclass
class Livros:
    def __init__(self,titulo,autor,numero_de_paginas,preco):
        self.titulo=titulo
        self.autor=autor
        self.numero_de_paginas=numero_de_paginas
        self.preco=preco

QUANTIDADE_LIVROS =2
livros=[]

for i in range(QUANTIDADE_LIVROS):
    titulo =input("Digite o titulo do livro: ")
    autor=input("Digite o nome do autor: ")
    numero_de_paginas=input("Digite o numero de paginas do livro: ")
    preco=input("Digite o preço do livro: ")
    os.system("cls || clear")

    livros.append(Livros(titulo,autor,numero_de_paginas,preco))


for i in livros:
    print(f"Livro: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Número de paginas: {i.numero_de_paginas}")
    print(f"Preço do livro: {i.preco}")
    print("\n")