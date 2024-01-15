tamanho = int(input("Digite o tamanho da lista:"))
lista = []
for i in range(tamanho):
  num = int(input("Digite um número:"))
  lista.append(num) 
  for i in range(len(lista)):
    atual = lista[i]
    j = i - 1
    while(j >= 0 and lista[j] > lista[j+1]):
        lista[j+1] = lista[j]
        lista[j] = atual
        j = j - 1        
print(lista)
        
        