# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vogal")
elif letra.isalpha():
    print("Consoante")
else:
    print("Não é uma letra válida")
