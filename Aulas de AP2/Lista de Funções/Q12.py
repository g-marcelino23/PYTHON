import random


def embaralhar_string(s):
    # Converte todos os caracteres para minúsculas
    s = s.lower()

    # Converte a string em uma lista de caracteres
    caracteres = list(s)

    # Embaralha os caracteres
    random.shuffle(caracteres)

    # Junta os caracteres embaralhados de volta em uma string
    string_embaralhada = ''.join(caracteres)

    return string_embaralhada


# Exemplo de uso
palavra_original = input("Digite uma palavra: ")
palavra_embaralhada = embaralhar_string(palavra_original)

print(f"A palavra embaralhada é: {palavra_embaralhada}")
