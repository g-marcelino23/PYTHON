'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()

par_impar = "par" if resultado % 2 == 0 else "ímpar"

positivo_negativo = "positivo" if resultado > 0 else "negativo"

inteiro_decimal = "inteiro" if resultado == round(resultado) else "decimal"

print(f"Resultado da operação: {resultado}")
print(f"O número é {par_impar}, {positivo_negativo} e {inteiro_decimal}.")
