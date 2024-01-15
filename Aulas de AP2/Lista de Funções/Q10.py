import random

def joga_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():
    # Primeira jogada
    primeira_jogada = joga_dados()
    print(f"Você rolou um total de {primeira_jogada}.")

    if primeira_jogada in (7, 11):
        print("Você ganhou! É um natural.")
        return True
    elif primeira_jogada in (2, 3, 12):
        print("Você perdeu! É um craps.")
        return False
    else:
        print(f"Seu ponto é {primeira_jogada}. Continue jogando.")

    # Continuar jogando até ganhar ou perder
    while True:
        proxima_jogada = joga_dados()
        print(f"Você rolou um total de {proxima_jogada}.")

        if proxima_jogada == primeira_jogada:
            print("Você ganhou! Tirou o ponto novamente.")
            return True
        elif proxima_jogada == 7:
            print("Você perdeu! Tirou um 7 antes de atingir o ponto novamente.")
            return False

# Iniciar o jogo
print("Bem-vindo ao jogo de Craps!")
while True:
    continuar = input("Deseja jogar? (s/n): ").lower()
    if continuar != 's':
        print("Obrigado por jogar. Até mais!")
        break

    if craps():
        print("Parabéns! Você ganhou.")
    else:
        print("Que pena! Você perdeu.")
