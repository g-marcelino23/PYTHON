def imprime_padrao(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="   ")
        print()

n = int(input("Informe o valor de n: "))
imprime_padrao(n)
