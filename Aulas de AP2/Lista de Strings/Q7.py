'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
A)quantos espaços em branco existem na frase.
B)quantas vezes aparecem as vogais a, e, i, o, u.'''

frase = input("Digite uma frase: ")

espacos_em_branco = frase.count(" ")

vogais = "aeiouAEIOU"
contador_vogais = sum(map(frase.lower().count, vogais))

print(f"Quantidade de espaços em branco: {espacos_em_branco}")
print(f"Quantidade de vogais: {contador_vogais}")
