'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
 de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

quantidade_morangos = float(input("Digite a quantidade (em Kg) de morangos: "))
quantidade_macas = float(input("Digite a quantidade (em Kg) de maçãs: "))

preco_morango = 2.50 if quantidade_morangos <= 5 else 2.20
preco_maca = 1.80 if quantidade_macas <= 5 else 1.50

valor_total = (quantidade_morangos * preco_morango) + (quantidade_macas * preco_maca)

if (quantidade_morangos + quantidade_macas) > 8 or valor_total > 25:
    desconto = 0.10 * valor_total
    valor_total -= desconto

print(f"Valor a ser pago: R$ {valor_total:.2f}")
