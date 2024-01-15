'''nome = input("Nome do atleta: ")

while nome != "":
    saltos = []

    for i in range(7):
        salto = float(input(f"{i + 1}º Salto: "))
        saltos.append(salto)

    melhor_salto = max(saltos)
    pior_salto = min(saltos)
    media_saltos = sum(saltos) / len(saltos)

    print(f"Melhor salto: {melhor_salto} m")
    print(f"Pior salto: {pior_salto} m")
    print(f"Média dos demais saltos: {media_saltos:.1f} m")

    nome = input("\nNome do próximo atleta: ")

print("Programa encerrado.")


atleta = input("Escreva o nome do atleta: ")
maiorNota = 0
menorNota = float('inf')  # Defina a menorNota como infinito para garantir que qualquer nota seja menor
soma = 0

for c in range(0, 7):
    nota = float(input("Digite uma nota: "))
    if nota > maiorNota:
        maiorNota = nota
    if nota < menorNota:
        menorNota = nota
    soma += nota

media = (soma - menorNota - maiorNota) / 5
print("Nome do Atleta:", atleta)
print("Maior Nota:", maiorNota)
print("Menor Nota:", menorNota)
print(f"Média das 5 notas: {media:.2f}")'''

atleta = input("Escreva o nome do atleta: ")
maiorNota = 0
soma = 0

# Obtenha a primeira nota e defina-a como a maior e a menor nota inicialmente
primeiraNota = float(input("Digite a primeira nota: "))
maiorNota = primeiraNota
menorNota = primeiraNota
soma += primeiraNota

for c in range(1, 7):  # Começando em 1 porque já obtivemos a primeira nota
    nota = float(input("Digite uma nota: "))
    if nota > maiorNota:
        maiorNota = nota
    if nota < menorNota:
        menorNota = nota
    soma += nota

media = (soma - menorNota - maiorNota) / 5
print("Nome do Atleta:", atleta)
print("Maior Nota:", maiorNota)
print("Menor Nota:", menorNota)
print(f"Média das 5 notas: {media:.2f}")

