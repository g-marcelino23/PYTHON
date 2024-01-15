''' Faça um programa que leia 2 strings e informe o conteúdo delas
 seguido do seu comprimento. Informe também se as duas strings possuem
  o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

string1 = input("String 1: ")
string2 = input("String 2: ")

tamanho_string1 = len(string1)
tamanho_string2 = len(string2)

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Tamanho de \"{string1}\": {tamanho_string1} caracteres")
print(f"Tamanho de \"{string2}\": {tamanho_string2} caracteres")

diferenca_tamanhos = tamanho_string1 - tamanho_string2
print(f"As duas strings são de tamanhos " + ("diferentes." * (diferenca_tamanhos != 0)))

conteudo_diferente = string1 != string2
print(f"As duas strings possuem conteúdo " + ("diferente." * conteudo_diferente))
