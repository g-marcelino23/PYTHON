def imprimir(n):
    for i in range(1, n + 1):
        linha = " ".join(str(j) for j in range(1, i + 1))
        print(linha)

n = int(input("Digite um número inteiro n: "))
imprimir(n)
