'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de
notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valor_saque = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor de saque inválido.")
else:
    notas_100 = valor_saque // 100
    valor_saque %= 100

    notas_50 = valor_saque // 50
    valor_saque %= 50

    notas_10 = valor_saque // 10
    valor_saque %= 10

    notas_5 = valor_saque // 5
    valor_saque %= 5

    notas_1 = valor_saque

    print(f"Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de 100 reais")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de 50 reais")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de 10 reais")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de 5 reais")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de 1 real")
