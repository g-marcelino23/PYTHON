'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split('/'))

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[2] = 29

if mes < 1 or mes > 12:
    print("Data inválida.")
elif dia < 1 or dia > dias_por_mes[mes]:
    print("Data inválida.")
else:
    print("Data válida.")
