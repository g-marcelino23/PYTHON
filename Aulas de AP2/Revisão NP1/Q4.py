while True:
    num = input("Digite um número inteiro (ou 0 para sair): ")

    if num == "0":
        break

    num = int(num)
    if num < 2 or any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
        print(f"{num} não é um número primo.")
    else:
        print(f"{num} é um número primo.")
