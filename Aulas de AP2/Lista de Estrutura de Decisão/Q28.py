'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão
Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça
o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

print("Tipos de carne disponíveis:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

tipo_carne = int(input("Digite o número correspondente ao tipo de carne desejado: "))
quantidade_carne = float(input("Digite a quantidade (em Kg) de carne: "))
pagamento_cartao = input("A compra será feita com o cartão Tabajara? (S para sim, N para não): ").upper()

if tipo_carne == 1:
    tipo_carne_nome = "Filé Duplo"
    preco_carne = 4.90 if quantidade_carne <= 5 else 5.80
elif tipo_carne == 2:
    tipo_carne_nome = "Alcatra"
    preco_carne = 5.90 if quantidade_carne <= 5 else 6.80
elif tipo_carne == 3:
    tipo_carne_nome = "Picanha"
    preco_carne = 6.90 if quantidade_carne <= 5 else 7.80
else:
    print("Tipo de carne inválido.")
    exit()

total_compra = quantidade_carne * preco_carne

if pagamento_cartao == "S":
    desconto = 0.05 * total_compra
    valor_desconto = "5%"
else:
    desconto = 0
    valor_desconto = "0%"

valor_a_pagar = total_compra - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne_nome}")
print(f"Quantidade: {quantidade_carne:.2f} Kg")
print(f"Preço por Kg: R$ {preco_carne:.2f}")
print(f"Total: R$ {total_compra:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if pagamento_cartao == 'S' else 'Outro método'}")
print(f"Valor do desconto: {valor_desconto}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
