"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total."""

import math

area_Pintada = float(input('Digite o tamanho em metros quadrados da área a ser pintada:'))

litros_Necessarios = area_Pintada / 3

quantidades_Latas = litros_Necessarios / 18

quantidades_Latas = math.ceil(quantidades_Latas)

preco_Lata = 80.00
preco_Total = quantidades_Latas * preco_Lata

print(f"Você precisará de {quantidades_Latas} latas de tinta")
print(f"O preço total é: R$ {preco_Total:.2f}")