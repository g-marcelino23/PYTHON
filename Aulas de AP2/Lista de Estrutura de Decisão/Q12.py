'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
]e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.1
else:
    desconto_ir = salario_bruto * 0.2

desconto_sindicato = salario_bruto * 0.03

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_sindicato

salario_liquido = salario_bruto - total_descontos

print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("Desconto do Imposto de Renda: R$ {:.2f}".format(desconto_ir))
print("Desconto do Sindicato: R$ {:.2f}".format(desconto_sindicato))
print("FGTS depositado pela empresa: R$ {:.2f}".format(fgts))
print("Total de descontos: R$ {:.2f}".format(total_descontos))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))
