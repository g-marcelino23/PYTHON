from datetime import datetime


def data_por_extenso(data_str):
    try:
        # Tenta converter a string de data para um objeto datetime
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")

        # Obtém os componentes da data
        dia = data_obj.day
        mes = data_obj.strftime("%B")  # Obtém o nome do mês por extenso
        ano = data_obj.year

        # Retorna a data formatada
        return f"{dia} de {mes} de {ano}"
    except ValueError:
        # Retorna NULL (None) se a data for inválida
        return None


# Exemplo de uso
data_input = input("Digite uma data (DD/MM/AAAA): ")
data_formatada = data_por_extenso(data_input)

if data_formatada is not None:
    print(f"A data por extenso é: {data_formatada}")
else:
    print("Data inválida. Retornando NULL.")
