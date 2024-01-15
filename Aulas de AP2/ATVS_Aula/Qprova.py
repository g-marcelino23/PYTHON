matriz = []
soma_ultima_coluna = 0

print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o elemento da posição ({i + 1},{j + 1}): "))
        linha.append(elemento)

        if j == 2:
            soma_ultima_coluna += elemento

    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

print(f"Soma da última coluna: {soma_ultima_coluna}")




