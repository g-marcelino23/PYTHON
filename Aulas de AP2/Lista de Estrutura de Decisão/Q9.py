# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

numeros = [numero1, numero2, numero3]

numeros.sort(reverse=True)

print("Os números em ordem decrescente são:", numeros)
