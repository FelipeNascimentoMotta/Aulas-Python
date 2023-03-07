
import os


acaoEscolida = ''
lista=[]
while(acaoEscolida != 'S'):
    os.system('cls')
    acaoEscolida = input("Selecione uma ação para sua lista: [L]istar, [A]pagar, [I]nserir, [S]air: ")

    
    if acaoEscolida.upper().startswith('L'):
        for item in enumerate(lista):
            print(item)
    elif acaoEscolida.upper().startswith('A'):
        try:
            lista.pop(int(input("Qual item deseja retirar: ")))
        except:
            print('Indice não encontrado para exclusão')
    elif acaoEscolida.upper().startswith('I'):
        lista.append(input("Oque deseja inserir na lista: "))
    elif acaoEscolida.upper().startswith('S'):
        break
    else:
        print('Digite uma ação valida')
