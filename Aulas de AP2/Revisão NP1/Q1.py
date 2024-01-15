matriz = [[0,0,0],[0,0,0],[0,0,0]]
diagonal = 0
pares = 0
somaTudo = 0
maior = 0
menor = float("inf")

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o elemento da linha{linha} coluna{coluna} \n"))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]}]", end="")
    print()

for i in range(3):
    if matriz[i][i]:
        diagonal += matriz[i][i]
print(f"A matriz apresenta a soma da diagonal principal {diagonal}")


for linha in range(0,3):
    for coluna in range(0,3):
        somaTudo+=matriz[linha][coluna]
print(f"A soma de tudo {somaTudo}")
media = somaTudo/9
print(f"A média é {media}")

for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
print(f"O maior {maior}")

for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] < menor:
            menor = matriz[linha][coluna]
print(f"O menor {menor}")
