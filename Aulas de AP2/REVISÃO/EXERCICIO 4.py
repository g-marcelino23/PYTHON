def insertion_sort_com_contagem(arr):
    trocas = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1
        arr[j + 1] = key
    return trocas
