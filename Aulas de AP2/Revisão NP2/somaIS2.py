def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

# Solicita ao usuário que insira os números da lista
entrada = input("Digite os números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

# Chama a função de ordenação por inserção
insertion_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)
