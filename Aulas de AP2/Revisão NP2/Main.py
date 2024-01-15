'''
*  CONTAGEM IS *

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

_______________________________________________________________________________________________________________________

* FUNÇÃO IS *

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

________________________________________________________________________________________________________________________

 * INSERTION REVERSO *

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

________________________________________________________________________________________________________________________

* INVERTER FRASE *

def inverter(frase):

    frase_invertida = frase[::-1]
    return frase_invertida

entrada = input("Digite uma frase ou nome: ")

frase_invertida = inverter(entrada)

print("Frase ou nome invertido:", frase_invertida)

________________________________________________________________________________________________________________________

* ORDENAÇÃO PARCIAL *

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

________________________________________________________________________________________________________________________

* PADRAO *

def imprime_padrao(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="   ")
        print()

n = int(input("Informe o valor de n: "))
imprime_padrao(n)

________________________________________________________________________________________________________________________

* PRIMO *

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

num = int(input("Digite um número inteiro: "))

if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

________________________________________________________________________________________________________________________

* SELECTION SEM MUDAR *

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

________________________________________________________________________________________________________________________

* SOMA *

def soma_lista(lista):
    if not lista:  # Verifica se a lista está vazia
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# Exemplo de uso
minha_lista = [1,2,3,4,5]
resultado = soma_lista(minha_lista)
print(f"A soma dos elementos da lista é: {resultado}")

________________________________________________________________________________________________________________________

* SOMA IS *

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

# Lista original
numeros = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]

# Chama a função de ordenação por inserção
insertion_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)

________________________________________________________________________________________________________________________

* SOMA IS2*

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

________________________________________________________________________________________________________________________

* SOMA RECURSAO *

def soma_lista_recursivamente(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista_recursivamente(lista[1:])

lista = [2, 4, 6, 8, 12, 20, 32, 40, 51]

resultado = soma_lista_recursivamente(lista)

print("A soma dos elementos da lista é:", resultado)

________________________________________________________________________________________________________________________

* SOMA SS *

def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]

# Lista original
numeros = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]

# Chama a função de ordenação por seleção
selection_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)

________________________________________________________________________________________________________________________

* SOMA SS2 *

def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]

# Solicita ao usuário que insira os números da lista
entrada = input("Digite os números separados por espaço: ")
numeros = [int(numero) for numero in entrada.split()]

# Chama a função de ordenação por seleção
selection_sort(numeros)

# Imprime a lista ordenada
print("Lista ordenada:")
print(numeros)

________________________________________________________________________________________________________________________

* PLANILHA *

import openpyxl

planilha = openpyxl.Workbook()
pagina = planilha.active

pagina["A1"] = "FRUTAS"
pagina["A2"] = "Banana"
pagina["A3"] = "Mamão"
pagina["A4"] = "Maçã"

pagina["B1"] = "PREÇO"
pagina["B2"] = "R$ 5,00"
pagina["B3"] = "R$ 6,00"
pagina["B4"] = "R$ 8,00"

# Lista de frutas e preços
frutas = ["Banana", "Mamão", "Maçã"]
precos = [5.0, 6.0, 8.0]

# Encontre a fruta mais cara
fruta_mais_cara = ""
preco_mais_alto = 0

for i in range(len(frutas)):
    preco_str = pagina["B" + str(i + 2)].value  # Obtenha o valor da célula B
    preco = float(preco_str.replace("R$", "").replace(",", "."))  # Converta o preço para float
    if preco > preco_mais_alto:
        preco_mais_alto = preco
        fruta_mais_cara = frutas[i]

planilha.save("SacolãoDoJoão.xlsx")
print("A fruta mais cara é:", fruta_mais_cara)
print("Preço mais alto:", "R$", preco_mais_alto)
print("Rodou")

________________________________________________________________________________________________________________________

* PAGAMENTO *

def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_a_pagar = valor_prestacao + multa + juros
        return valor_a_pagar


total_prestacoes_pagas = 0
valor_total_pagamento = 0

while True:
    valor_prestacao = float(input("Informe o valor da prestação (ou digite 0 para sair): "))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input("Informe o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

    total_prestacoes_pagas += 1
    valor_total_pagamento += valor_a_pagar

print(f"Relatório do dia:")
print(f"Total de prestações pagas: {total_prestacoes_pagas}")
print(f"Valor total pago: R$ {valor_total_pagamento:.2f}")




























'''