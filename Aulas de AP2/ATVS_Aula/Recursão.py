def soma_lista_recursivamente(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista_recursivamente(lista[1:])

lista = [2, 4, 6, 8, 12, 20, 32, 40, 51]

resultado = soma_lista_recursivamente(lista)

print("A soma dos elementos da lista é:", resultado)

'''
def inverter(frase):

    frase_invertida = frase[::-1]
    return frase_invertida

entrada = input("Digite uma frase ou nome: ")

frase_invertida = inverter(entrada)

print("Frase ou nome invertido:", frase_invertida)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Se a lista tem 0 ou 1 elemento, ela já está ordenada

    pivot = arr[0]  # Escolhe o primeiro elemento como pivô
    lesser, equal, greater = [], [], []  # Inicializa listas vazias para menores, iguais e maiores

    # Percorre a lista original
    for num in arr:
        if num < pivot:
            lesser.append(num)  # Se o elemento for menor que o pivô, adiciona a 'lesser'
        elif num == pivot:
            equal.append(num)  # Se o elemento for igual ao pivô, adiciona a 'equal'
        else:
            greater.append(num)  # Se o elemento for maior que o pivô, adiciona a 'greater'

    # Chama recursivamente quick_sort nas listas 'lesser' e 'greater' e concatena com 'equal'
    return quick_sort(lesser) + equal + quick_sort(greater)

numbers = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]  # Lista de números a ordenar
sorted_numbers = quick_sort(numbers)  # Chama quick_sort para ordenar a lista
print(sorted_numbers)  # Imprime o resultado da lista ordenada

def is_prime(n, div=2):
    if n <= 1:
        return False
    if div * div > n:
        return True
    if n % div == 0:
        return False
    return is_prime(n, div + 1)

def main():
    numbers = []  # Inicializa uma lista vazia para armazenar os números

    while True:
        try:
            num = int(input("Digite um número inteiro (ou digite 0 para parar): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    for num in numbers:
        if is_prime(num):
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")

if __name__ == "__main__":
    main()
'''


