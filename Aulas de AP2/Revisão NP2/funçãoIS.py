lista = [50, 2, 15, 42, 5]


def sort(lista_desordenada):
    def insertion_sort(lista_desordenada):
        for i in range(1, len(lista_desordenada)):

            atual = lista_desordenada[i]
            j = i - 1

            while j >= 0 and atual < lista_desordenada[j]:
                lista_desordenada[j + 1], lista_desordenada[j] = lista_desordenada[j], lista_desordenada[j + 1]
                j -= 1

    def selection_sort(lista_desordenada):
        for i in range(len(lista_desordenada)):

            menor = i

            for j in range(i + 1, len(lista_desordenada)):
                if lista_desordenada[j] < lista_desordenada[menor]:
                    menor = j

            if menor != i:
                lista_desordenada[i], lista_desordenada[menor] = lista_desordenada[menor], lista_desordenada[i]

    if len(lista_desordenada) < 6:
        insertion_sort(lista_desordenada)
        print(f'Metodo utilizado: insertion sort')

    else:
        selection_sort(lista_desordenada)
        print("Metodo utilizado: selection sort")


sort(lista)
print(lista) 