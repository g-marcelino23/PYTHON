''' Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a)Para homens: (72.7*h) - 58
b)Para mulheres: (62.1*h) - 44.7 '''

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (H para homem, M para mulher): ")

if sexo == "H":
    peso_ideal = (72.7 * altura) - 58
    genero = "homem"
elif sexo == "M":
    peso_ideal = (62.1 * altura) - 44.7
    genero = "mulher"
else:
    print("Sexo inválido. Use H para homem ou M para mulher.")

print("O peso ideal para um(a) " + genero + " de altura", altura, "metros é:", round(peso_ideal, 2), "kg")
