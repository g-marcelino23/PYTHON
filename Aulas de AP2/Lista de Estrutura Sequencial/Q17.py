''' Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
 da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a)comprar apenas latas de 18 litros;
b)comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

area_para_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area_para_pintar / 6

latas_18_litros = int(litros_necessarios / 18)
galoes_3_6_litros = int(litros_necessarios / 3.6)

if litros_necessarios % 18 != 0:
    latas_18_litros += 1
if litros_necessarios % 3.6 != 0:
    galoes_3_6_litros += 1

preco_latas = latas_18_litros * 80
preco_galoes = galoes_3_6_litros * 25

print("Quantidade de tinta necessária:", litros_necessarios, "litros")

print("Opção 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas:", latas_18_litros)
print("Preço total: R$", preco_latas)

print("Opção 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões:", galoes_3_6_litros)
print("Preço total: R$", preco_galoes)
