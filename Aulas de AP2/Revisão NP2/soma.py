def soma_lista(lista):
    if not lista:  # Verifica se a lista está vazia
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# Exemplo de uso
minha_lista = [1,2,3,4,5]
resultado = soma_lista(minha_lista)
print(f"A soma dos elementos da lista é: {resultado}")



