'''Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado.'''

def digitos(numero):
    return len(str(numero))

numero = int(input("Digite um número inteiro: "))

quantidade_digitos = digitos(numero)
print(f"O número {numero} possui {quantidade_digitos} dígitos.")
