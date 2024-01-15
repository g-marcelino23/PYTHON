def desenhar_retangulo(linhas=1, colunas=1):
    # Limita os valores de linhas e colunas no intervalo [1, 20]
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            # Linhas superiores e inferiores do retângulo
            print('+' + '-' * (colunas - 2) + '+')
        else:
            # Linhas intermediárias do retângulo
            print('|' + ' ' * (colunas - 2) + '|')

# Exemplo de uso
try:
    linhas_input = int(input("Digite o número de linhas: "))
    colunas_input = int(input("Digite o número de colunas: "))
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
    linhas_input = 1
    colunas_input = 1

desenhar_retangulo(linhas_input, colunas_input)
