'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
 do usuário e imprima a data com o nome do mês por extenso.'''

meses = {
    "01": "janeiro", "02": "fevereiro", "03": "março",
    "04": "abril", "05": "maio", "06": "junho",
    "07": "julho", "08": "agosto", "09": "setembro",
    "10": "outubro", "11": "novembro", "12": "dezembro"
}

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = data_nascimento.split("/")

mes_extenso = meses[mes]

print(f"Data de nascimento: {dia} de {mes_extenso} de {ano}")
