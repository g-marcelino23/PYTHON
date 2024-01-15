'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input("Digite o nome (maior que 3 caracteres): ")
while len(nome) <= 3:
    print("Nome deve ter mais de 3 caracteres. Tente novamente.")
    nome = input("Digite o nome (maior que 3 caracteres): ")

idade = int(input("Digite a idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
    print("Idade deve estar entre 0 e 150. Tente novamente.")
    idade = int(input("Digite a idade (entre 0 e 150): "))

salario = float(input("Digite o salário (maior que zero): "))
while salario <= 0:
    print("Salário deve ser maior que zero. Tente novamente.")
    salario = float(input("Digite o salário (maior que zero): "))

sexo = input("Digite o sexo ('f' para feminino, 'm' para masculino): ")
while sexo not in ('f', 'm'):
    print("Sexo deve ser 'f' ou 'm'. Tente novamente.")
    sexo = input("Digite o sexo ('f' para feminino, 'm' para masculino): ")

estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ")
while estado_civil not in ('s', 'c', 'v', 'd'):
    print("Estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")
    estado_civil = input("Digite o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ")

print("Informações válidas. Cadastro realizado com sucesso!")
