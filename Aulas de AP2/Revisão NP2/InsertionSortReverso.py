def insertionSortRev(array):
    for i in range(len(array)):
        aux = array[i]
        j = i - 1

        while (j >= 0 and array[j] < aux):
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = aux
    return array


vetor = [13, 45, 23, 12, 2, 78, 90, 1]
print(insertionSortRev(vetor))