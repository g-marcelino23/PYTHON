def selectionSortIndices(array):
    n = len(array)
    vetor_indices = list(range(n))

    for i in range(n - 1, 0, -1):
        iMax = 0
        for j in range(1, i+1):
            if array[vetor_indices[j]] > array[vetor_indices[iMax]]:
                iMax = j

        vetor_indices[i], vetor_indices[iMax] = vetor_indices[iMax], vetor_indices[i]

    return vetor_indices

vetor = [13, 45, 23, 12, 2, 78, 90, 1]
vetor_indices = selectionSortIndices(vetor)

print("Vetor:", vetor)
print("Vetor de Índices:", vetor_indices)