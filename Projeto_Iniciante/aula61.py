"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import re
import random

#cpfCompleto ='746.824.890-70'#.replace('.','').replace('-','').replace(' ','')
cpfDigitado = input('Digite seu CPF: ')
cpfDigitado = False if cpfDigitado == '' else cpfDigitado
primeiroDigito = 0
segundoDigito = 0
multiplicador = 10

if cpfDigitado == False:
    cpfCompleto = ''
    for numero in range(9):
        cpfCompleto += str(random.randint(0,9))

    for numero in cpfCompleto:
            primeiroDigito+= int(numero)*multiplicador
            multiplicador -= 1

    primeiroDigito= ((primeiroDigito*10)%11)
    primeiroDigito = primeiroDigito if primeiroDigito <=9 else 0
    multiplicador = 11
    cpfDezDigitos = cpfCompleto + str(primeiroDigito)

    for numero in cpfDezDigitos:
        segundoDigito+= int(numero)*multiplicador
        multiplicador -= 1

    segundoDigito= ((segundoDigito*10)%11) 
    segundoDigito = segundoDigito if segundoDigito <=9 else 0
    print(f'CPF Gerado: {cpfDezDigitos+str(segundoDigito)}')

else:
    cpfCompleto = re.sub(r'[^0-9]', '',cpfDigitado)

    cpfCompleto = False if cpfCompleto == (cpfCompleto[0]*len(cpfCompleto)) else cpfCompleto
    if cpfCompleto != False:

        ultimos2Digitos = cpfCompleto[9] + cpfCompleto[10]
        cpfNoveDigitos = cpfCompleto[:9]
        cpfDezDigitos = cpfCompleto[:10]
        multiplicador = 10
        primeiroDigito = 0
        segundoDigito=0

        for numero in cpfNoveDigitos:
            primeiroDigito+= int(numero)*multiplicador
            multiplicador -= 1

        primeiroDigito= ((primeiroDigito*10)%11) 

        primeiroDigito = primeiroDigito if primeiroDigito <=9 else 0

        print(f"Primeiro digito é igual: {primeiroDigito}")

        multiplicador = 11

        for numero in cpfDezDigitos:
            segundoDigito+= int(numero)*multiplicador
            multiplicador -= 1

        segundoDigito= ((segundoDigito*10)%11) 
        segundoDigito = segundoDigito if segundoDigito <=9 else 0
        print(f"Segundo digito é igual: {segundoDigito}")
        print( "Cpf Valido" if str(primeiroDigito)+str(segundoDigito) == ultimos2Digitos  else "Cpf Invalido")
    else:
        print('Sequencia de numeros repetidas, CPF invalido')