def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_a_pagar = valor_prestacao + multa + juros
        return valor_a_pagar


total_prestacoes_pagas = 0
valor_total_pagamento = 0

while True:
    valor_prestacao = float(input("Informe o valor da prestação (ou digite 0 para sair): "))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input("Informe o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

    total_prestacoes_pagas += 1
    valor_total_pagamento += valor_a_pagar

print(f"Relatório do dia:")
print(f"Total de prestações pagas: {total_prestacoes_pagas}")
print(f"Valor total pago: R$ {valor_total_pagamento:.2f}")
