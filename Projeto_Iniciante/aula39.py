"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
nova_string = ''

contador = 0

while tamanho_nome > contador:
    nova_string+= '*'+nome[contador]
    contador+=1

nova_string+='*'
print(nova_string)