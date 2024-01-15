import openpyxl

planilha = openpyxl.Workbook()
pagina = planilha.active

pagina["A1"] = "FRUTAS"
pagina["A2"] = "Banana"
pagina["A3"] = "Mamão"
pagina["A4"] = "Maçã"

pagina["B1"] = "PREÇO"
pagina["B2"] = "R$ 5,00"
pagina["B3"] = "R$ 6,00"
pagina["B4"] = "R$ 8,00"

# Lista de frutas e preços
frutas = ["Banana", "Mamão", "Maçã"]
precos = [5.0, 6.0, 8.0]

# Encontre a fruta mais cara
fruta_mais_cara = ""
preco_mais_alto = 0

for i in range(len(frutas)):
    preco_str = pagina["B" + str(i + 2)].value  # Obtenha o valor da célula B
    preco = float(preco_str.replace("R$", "").replace(",", "."))  # Converta o preço para float
    if preco > preco_mais_alto:
        preco_mais_alto = preco
        fruta_mais_cara = frutas[i]

planilha.save("SacolãoDoJoão.xlsx")
print("A fruta mais cara é:", fruta_mais_cara)
print("Preço mais alto:", "R$", preco_mais_alto)
print("Rodou")
