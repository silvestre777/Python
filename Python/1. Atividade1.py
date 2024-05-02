import os

os.system ("cls || clear")

morango_kg = float(input ("Digite a quantidade em KG de morangos: "))
maca_kg = float (input("Digite a quantidade de maçã em KG: "))

if morango_kg <5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if maca_kg <5:
     preco_maca= 1.80
else:
    preco_maca = 1.50

    pesoTotal = morango_kg + maca_kg
    subTotal = (maca_kg * preco_maca) + (morango_kg * preco_morango)

    if pesoTotal > 8 or subTotal > 25:
        desconto = subTotal * 0.10

totalPagar = subTotal - desconto

print(f"Peso de morangos (em kg): {morango_kg}")
print(f"Peso da maçã (em kg): {maca_kg}")
print(f"Soma dos pesos (em kg): {pesoTotal}")
print(f"Subtotal: R$ {subTotal: .2f}")
print(f"Desconto: R$ {desconto: .2f}")
print(f"Total a pagar: R$ {totalPagar: .2f}")