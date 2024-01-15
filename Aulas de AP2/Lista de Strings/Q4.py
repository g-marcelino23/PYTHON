'''Modifique o programa anterior de forma a mostrar o nome em formato de escada.'''

nome = input("Digite o seu nome: ")

nome_maiusculo = nome.upper()

numeros = range(1, len(nome_maiusculo) + 1)

print("\n".join([nome_maiusculo[:i] for i in numeros]))
