def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]

# Lista original
numeros = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]

# Chama a função de ordenação por seleção
selection_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)
