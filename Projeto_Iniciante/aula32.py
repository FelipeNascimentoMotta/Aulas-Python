"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numeroDigitado =input('Digite um numero inteiro:')

# try:
#     numeroDigitado = int(numeroDigitado)
#     if numeroDigitado % 2 == 0:
#         print(f'O número digitado foi um número par {numeroDigitado}')
#     else:
#         print(f'O número digitado foi um número ímpar {numeroDigitado}')
# except:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horaAtual = input('Digite a hora do dia: ')

# try:
#     horaAtual = int(horaAtual)
#     if horaAtual <=11 and horaAtual >= 0:
#         print('Bom dia')
#     elif horaAtual >= 12 and horaAtual <= 17:
#         print('Boa tarde')
#     elif horaAtual >= 18 and horaAtual <= 23:
#         print('Boa noite')
#     else:
#         print('Você não digitou uma hora valida')
# except:
#     print('Você não digitou uma hora válida')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

if len(nome)<=4:
    print('Seu nome é curto')
elif len(nome)>=5 and len(nome)<=6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')
