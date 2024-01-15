def insertionSort(array, k):
    cont = 0
    for i in range(len(array)):
        aux = array[i]
        j = i - 1

        while (j >= 0 and array[j] >= aux and cont < k):
            array[j + 1] = array[j]
            j -= 1
            cont += 1

        array[j + 1] = aux
    return array


vetor = [13, 45, 23, 12, 2, 78, 90, 1]

k = int(input(
    f"Dado o seguinte vetor {vetor}, digite um valor inteiro k para que somente os primeiros k elementos sejam ordenados: "))

if k > len(vetor):
    k = len(vetor)

print(insertionSort(vetor[:k], k))