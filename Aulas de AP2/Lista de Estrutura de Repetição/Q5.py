'''Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

while True:
    try:
        populacao_a = int(input("Informe a população do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento do país A (%): ")) / 100
        populacao_b = int(input("Informe a população do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento do país B (%): ")) / 100

        if populacao_a <= 0 or taxa_crescimento_a <= 0 or populacao_b <= 0 or taxa_crescimento_b <= 0:
            print("Por favor, insira valores válidos maiores que zero.")
        else:
            anos = 0

            while populacao_a <= populacao_b:
                populacao_a *= 1 + taxa_crescimento_a
                populacao_b *= 1 + taxa_crescimento_b
                anos += 1

            print("Número de anos necessários:", anos)

            repetir = input("Deseja repetir a operação? (s/n): ")
            if repetir.lower() != 's':
                break

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")
