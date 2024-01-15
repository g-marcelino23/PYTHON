def escolher_algoritmo_ordenacao(arr):
    if len(arr) <= 20:
        insertion_sort_reverso(arr)
    else:
        selection_sort_indices(arr)
