'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois
inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para
a saída. Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se
é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos
valores de entrada todas as vezes que desejar.'''

import os
import time
def convert(hour, minute, period):
    if hour > 11:
        hour = hour - 12
        period = "A.M."
    elif 11 >= hour > 0:
        hour = 12 + hour
        period = "P.M."
    return show(hour, minute, period)
def show(hour, minute, period):
    if hour == 0:
        print(f"\nConverted hour: {hour}{hour}:{minute} {period}\n")
    else:
        print(f"\nConverted hour: {hour}:{minute} {period}\n")

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')
def principal():
    while True:
        time.sleep(2)
        limpaTela()

        period = str(input("Enter the period:\nA - A.M.\nP - P.M.\nYour option: ")).upper()

        if period == 'A':
            hour = int(input("Enter the hour: "))
            if hour > 11 or hour == 0:
                print("Invalid hour to the period!")
                continue
            minute = int(input("Enter the minute: "))
            if minute > 59 or minute < 0:
                print("Invalid minute!")
                continue
            convert(hour, minute, period)

        elif period == 'P':
            hour = int(input("Enter the hour: "))
            if 12 > hour > 0:
                print("Invalid hour to the period!")
                continue
            minute = int(input("Enter the minute: "))
            if minute > 59 or minute < 0:
                print("Invalid minute!")
                continue
            convert(hour, minute, period)

        else:
            print("Invalid period!")
            continue

        opc = int(input("Enter more values?\n1 - Continue\n2 - Stop\nYour option: "))
        if opc == 1:
            continue
        else:
            break
principal()
