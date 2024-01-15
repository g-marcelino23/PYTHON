'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

preco_alcool = 1.90
preco_gasolina = 2.50

if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_total = litros_vendidos * (preco_alcool - (preco_alcool * desconto))
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_total = litros_vendidos * (preco_gasolina - (preco_gasolina * desconto))

print(f"Total a pagar: R$ {valor_total:.2f}")
