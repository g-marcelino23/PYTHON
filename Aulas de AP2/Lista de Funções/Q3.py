'''Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos.'''


def soma(a, b, c):
    resultado = a + b + c
    return resultado

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma = soma(n1, n2, n3)

print(f"A soma dos três números é: {soma}")

