'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a)o produto do dobro do primeiro com metade do segundo .
b)a soma do triplo do primeiro com o terceiro.
c)o terceiro elevado ao cubo.'''

numero_um = int(input("Digite o primeiro número inteiro: "))
numero_dois = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

resultado1 = (numero_um * 2) * (numero_dois / 2)
resultado2 = (numero_um * 3) + numero_real
resultado3 = numero_real ** 3

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro elevado ao cubo é:", resultado3)
