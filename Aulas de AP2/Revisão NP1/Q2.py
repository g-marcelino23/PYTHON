matriz1 = []
print("Preencha a primeira matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f'Digite o elemento [{i+1}][{j+1}]: '))
        linha.append(elemento)
    matriz1.append(linha)

matriz2 = []
print("\nPreencha a segunda matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f'Digite o elemento [{i+1}][{j+1}]: '))
        linha.append(elemento)
    matriz2.append(linha)
    
soma_diagonal1 = 0
soma_diagonal2 = 0
for i in range(3):
    soma_diagonal1 += matriz1[i][i]
    soma_diagonal2 += matriz2[i][i]

resultado = soma_diagonal1 * soma_diagonal2

print("\nSoma da diagonal principal da primeira matriz:", soma_diagonal1)
print("Soma da diagonal principal da segunda matriz:", soma_diagonal2)
print("Resultado da multiplicação das somas das diagonais:", resultado)
