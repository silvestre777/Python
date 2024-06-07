# Solicite que o usuário informe o valor de um produto e a forma de pagamento.
# 1 - Pagamento à vista;
# 2 - Pagamento à prazo.

#Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão informe o mesmo valor do produto.

#Se for escolhida a opção de pagamento à prazo, solicite que o usuário digite a quantidade de parcelas que ele deseja pagar. 

# -------------------------------------------------------------

import os
os.system("cls || clear")

# Declarando variáveis.
desconto = 0
preco_final = 0
preco_parcelado = 0

print("Solicitando dados para o usuário.")
preco_produto = int(input("Digite o valor do produto: "))

print("\nEscolha uma das formas de pagamento abaixo.")
print("1 - pagamento a vista")
print("2 - pagamento a prazo")
opcao = int(input("Informe a opção desejada: "))

match (opcao):
    case 1:
        os.system("cls || clear")
        desconto = preco_produto * 0.10
        preco_final = preco_produto - desconto

        print(f"\nPreço do produto: R$ {preco_produto}")
        print(f"Forma de pagamento: a vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total a pagar: R$ {preco_final}")
    case 2:
        os.system("cls || clear")
        parcelas = int(input("\nDigite a quantidade de parcelas: "))

        preco_parcelado = preco_produto / parcelas
        preco_final = preco_produto

        print(f"\nPreço do produto: R$ {preco_produto}")
        print(f"Forma de pagamento: a prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor por parcela: R$ {preco_parcelado:.2f)}")
        print(f"Total a prazo: R$ {preco_final:.2f}")
    case _:
        print("Opção inválida! \n")