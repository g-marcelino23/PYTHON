'''def insertion_sort_reverse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Exemplo de uso:
lista = [12, 11, 13, 5, 6]
insertion_sort_reverse(lista)
print("Lista ordenada em ordem decrescente:", lista)'''

def insertion_sort_reverse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def main():
    n = int(input("Digite o número de elementos na lista: "))
    lista = []

    for i in range(n):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        lista.append(elemento)

    insertion_sort_reverse(lista)
    print("Lista ordenada em ordem decrescente:", lista)

if __name__ == "__main__":
    main()

