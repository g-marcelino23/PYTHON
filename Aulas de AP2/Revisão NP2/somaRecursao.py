def soma_lista_recursivamente(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista_recursivamente(lista[1:])

lista = [2, 4, 6, 8, 12, 20, 32, 40, 51]

resultado = soma_lista_recursivamente(lista)

print("A soma dos elementos da lista é:", resultado)