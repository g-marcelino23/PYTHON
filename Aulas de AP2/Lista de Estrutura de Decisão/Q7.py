# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior_numero = max(numero1, numero2, numero3)
menor_numero = min(numero1, numero2, numero3)

print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)
