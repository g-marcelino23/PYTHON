def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

# Lista original
numeros = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]

# Chama a função de ordenação por inserção
insertion_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)
