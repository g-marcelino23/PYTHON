'''Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.'''

def inverter(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    reverso = int(reverso_str)
    return reverso
  
num = int(input("Digite um número inteiro: "))

numero_invertido = inverter(num)
print(f"O reverso de {num} é: {numero_invertido}")
