def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]

# Solicita ao usuário que insira os números da lista
entrada = input("Digite os números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

# Chama a função de ordenação por seleção
selection_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)
