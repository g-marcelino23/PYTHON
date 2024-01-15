'''Faça um programa com uma função chamada somaImposto. A função possui dois
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa
em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def Imposto(taxaImposto, custo):
    custo_imposto = custo + (custo * (taxaImposto / 100))
    return custo_imposto

taxa = float(input("Digite a taxa de imposto (em porcentagem): "))
item = float(input("Digite o custo do item: "))

custo_total = Imposto(taxa, item)

print(f"O custo total com imposto é: R$ {custo_total:.2f}")
