'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número fora do intervalo válido.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    texto_centenas = "centenas" if centenas > 1 else "centena"
    texto_dezenas = "dezenas" if dezenas > 1 else "dezena"
    texto_unidades = "unidades" if unidades > 1 else "unidade"

    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} {texto_centenas}"

    if dezenas > 0:
        if resultado != "":
            resultado += ", "
        resultado += f"{dezenas} {texto_dezenas}"

    if unidades > 0:
        if resultado != "":
            if centenas == 0 and dezenas == 0:
                resultado += " e "
            else:
                resultado += ", "
        resultado += f"{unidades} {texto_unidades}"

    print(resultado)
