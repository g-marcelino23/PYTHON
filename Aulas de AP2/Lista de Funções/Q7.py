def valorPagamento(valor_prestacao, dias_atraso):
    # Calcula o valor a ser pago considerando multa e juros
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        return valor_prestacao + multa + juros


def relatorio_do_dia(total_prestacoes, valor_total):
    print("\nRelatório do Dia:")
    print(f"Quantidade de prestações pagas: {total_prestacoes}")
    print(f"Valor total recebido: R${valor_total:.2f}")


# Inicialização das variáveis
total_prestacoes_dia = 0
valor_total_dia = 0

while True:
    try:
        # Solicita ao usuário o valor da prestação
        valor_prestacao = float(input("Digite o valor da prestação (ou 0 para encerrar): "))

        # Verifica se o usuário deseja encerrar o programa
        if valor_prestacao == 0:
            break

        # Solicita ao usuário o número de dias em atraso
        dias_atraso = int(input("Digite o número de dias em atraso: "))

        # Calcula o valor a ser pago
        valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)

        # Exibe o valor a ser pago
        print(f"Valor a ser pago: R${valor_a_pagar:.2f}")

        # Atualiza o relatório do dia
        total_prestacoes_dia += 1
        valor_total_dia += valor_a_pagar

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Exibe o relatório final do dia
relatorio_do_dia(total_prestacoes_dia, valor_total_dia)
