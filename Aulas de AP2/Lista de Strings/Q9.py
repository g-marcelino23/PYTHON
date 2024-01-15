'''Desenvolva um programa que solicite a digitação de um número de CPF
no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através
 da validação dos dígitos verificadores edos caracteres de formatação.'''

def validarCPF(cpf):
    return cpf.isdigit()


def principal():
    while True:
        cpf = input("Digite seu cpf: ").replace(' ', '')
        if len(cpf) != 11:
            print("tamanho do cpf inválido!\nDigite novamente")
            continue
        if validarCPF(cpf) is True:
            print("CPF é válido!")
            break
        else:
            print("CPF é inválido!")
            continue


principal()