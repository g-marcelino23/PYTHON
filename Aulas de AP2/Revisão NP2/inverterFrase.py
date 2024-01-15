def inverter(frase):

    frase_invertida = frase[::-1]
    return frase_invertida

entrada = input("Digite uma frase ou nome: ")

frase_invertida = inverter(entrada)

print("Frase ou nome invertido:", frase_invertida)