"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']
contador = 0

for nome in lista:
    print(contador,nome, type(nome))
    contador += 1

contador = 0
for nome in lista:
    lista[contador] = str(contador)+' '+nome
    print(lista[contador], type(nome))
    contador += 1


"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))