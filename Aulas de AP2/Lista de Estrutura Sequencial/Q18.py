''' Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tamanho_arquivo_mbits = tamanho_arquivo_mb * 8
tempo_em_segundos = tamanho_arquivo_mbits / velocidade_internet_mbps
tempo_em_minutos = tempo_em_segundos / 60

print("Tempo aproximado de download:", round(tempo_em_minutos, 2), "minutos")
