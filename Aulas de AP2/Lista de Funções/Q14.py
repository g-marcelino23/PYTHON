from itertools import permutations

def eh_quadrado_magico(matriz):
    # Verifica se a soma das linhas, colunas e diagonais é a mesma
    s = sum(matriz[0])
    for i in range(1, len(matriz)):
        if sum(matriz[i]) != s:
            return False
    for j in range(len(matriz[0])):
        if sum(matriz[i][j] for i in range(len(matriz))) != s:
            return False
    if sum(matriz[i][i] for i in range(len(matriz))) != s or \
       sum(matriz[i][len(matriz) - i - 1] for i in range(len(matriz))) != s:
        return False
    return True

def mostrar_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados_magicos = []

    # Gera todas as permutações possíveis
    permutacoes = permutations(numeros)

    for permutacao in permutacoes:
        # Converte a permutação em uma matriz 3x3
        matriz = [list(permutacao[i:i+3]) for i in range(0, 9, 3)]

        # Verifica se é um quadrado mágico
        if eh_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)

    # Mostra os quadrados mágicos encontrados
    for quadrado in quadrados_magicos:
        print("Quadrado Mágico:")
        for linha in quadrado:
            print(" ".join(map(str, linha)))
        print()

# Chama a função para mostrar os quadrados mágicos
mostrar_quadrados_magicos()
