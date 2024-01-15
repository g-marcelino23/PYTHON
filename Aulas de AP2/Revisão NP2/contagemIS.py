def insertionSortTrocas(array):
    cont = 0
    for i in range(len(array)):
        aux = array[i]
        j = i - 1

        while (j >= 0 and array[j] >= aux):
            array[j + 1] = array[j]
            cont += 1
            j -= 1

        array[j + 1] = aux

    return cont


vetor = [13, 45, 23, 12, 2, 78, 90, 1]

print(f"O vetor: {vetor} precisou de {insertionSortTrocas(vetor)} trocas para ser ordenado.")