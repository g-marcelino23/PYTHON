''' a = "Hello, world!"
print(a[7:12])

txt = "The best things in life are free!"
print("free" in txt)

txt = "Hello, World!"
print("Hello" in txt)

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.split(","))

a = 330
b = 330

print("A") if a > b else pri("=") if a == b else print("B")



numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

print("Números lidos:")
for numero in numeros:
    print(numero)

relatorio = []  # Cria uma lista vazia para armazenar informações do relatório.
total_prestacoes = 0  # Inicializa a quantidade total de prestações pagas.
total_valor_pago = 0  # Inicializa o valor total pago.

while True:
    valor_prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))

    if valor_prestacao == 0:
        break  # Encerra o loop se o valor da prestação for 0.

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    if dias_atraso <= 0:
        valor_a_pagar = valor_prestacao  # Se não houver atraso, o valor a ser pago é igual ao valor da prestação.
    else:
        multa = valor_prestacao * 0.03  # Calcula a multa de 3% sobre o valor da prestação.
        juros = valor_prestacao * (0.001 * dias_atraso)  # Calcula os juros de 0.1% por dia de atraso.
        valor_a_pagar = valor_prestacao + multa + juros  # Calcula o valor a ser pago.

    relatorio.append((valor_prestacao, valor_a_pagar))  # Adiciona as informações do pagamento ao relatório.

    total_prestacoes += 1  # Incrementa a quantidade total de prestações pagas.
    total_valor_pago += valor_a_pagar  # Incrementa o valor total pago.

    print(f"Valor a ser pago: R${valor_a_pagar:.2f}\n")  # Exibe o valor a ser pago formatado.

print("\nRelatório do dia:")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total pago: R${total_valor_pago:.2f}")  # Exibe o valor total pago formatado.

combust = str(input("Digite qual combustível deseja: A - Álcool e G - Gasolina: ")).upper()
vendLitros = int(input("Digite a quantidade de litros que deseja colocar: "))
alcool = 1.90
gasolina = 2.50

if combust == 'A' and vendLitros <= 20.0:
    desconto = 0.03 * alcool
    precoLitro = alcool * vendLitros
    precoTotal = precoLitro - desconto

elif combust == 'A' and vendLitros > 20.0:
    desconto = 0.05 * alcool
    precoLitro = alcool * vendLitros
    precoTotal = precoLitro - desconto

elif combust == 'G' and vendLitros <= 20.0:
    desconto = 0.04 * gasolina
    precoLitro = gasolina * vendLitros
    precoTotal = precoLitro - desconto


elif combust == 'G' and vendLitros > 20.0:
    desconto = 0.06 * gasolina
    precoLitro = gasolina * vendLitros
    precoTotal = precoLitro - desconto

print(f"Combustível escolhido: {combust}")
print(f"Valor a ser pago: R$ {precoTotal:.2f}")

combust = input("Digite qual combustível deseja: A - Álcool e G - Gasolina: ").upper()
vendLitros = float(input("Digite a quantidade de litros que deseja colocar: "))
alcool = 1.90
gasolina = 2.50

if combust == 'A' and vendLitros <= 20.0:
    desconto = 0.03 * vendLitros
    precoLitro = alcool * vendLitros
    precoTotal = precoLitro - desconto

elif combust == 'A' and vendLitros > 20.0:
    desconto = 0.05 * vendLitros
    precoLitro = alcool * vendLitros
    precoTotal = precoLitro - desconto

elif combust == 'G' and vendLitros <= 20.0:
    desconto = 0.04 * vendLitros
    precoLitro = gasolina * vendLitros
    precoTotal = precoLitro - desconto

elif combust == 'G' and vendLitros > 20.0:
    desconto = 0.06 * vendLitros
    precoLitro = gasolina * vendLitros
    precoTotal = precoLitro - desconto

print(f"Combustível escolhido: {combust}")
print(f"Valor a ser pago: R$ {precoTotal:.2f}")

combust = input("Digite qual combustível deseja: A - Álcool e G - Gasolina: ").upper()
vendLitros = float(input("Digite a quantidade de litros que deseja colocar: "))
alcool = 1.90
gasolina = 2.50

if combust == 'A':
    if vendLitros <= 20.0:
        desconto = 0.03 * alcool * vendLitros
    else:
        desconto = 0.05 * alcool * vendLitros
    precoLitro = alcool
elif combust == 'G':
    if vendLitros <= 20.0:
        desconto = 0.04 * gasolina * vendLitros
    else:
        desconto = 0.06 * gasolina * vendLitros
    precoLitro = gasolina
else:
    print("Opção de combustível inválida")
    exit()

precoTotal = precoLitro * vendLitros - desconto

print(f"Combustível escolhido: {combust}")
print(f"Valor a ser pago: R$ {precoTotal:.2f}")'''


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))





