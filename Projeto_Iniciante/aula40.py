""" Calculadora com while """
while True:
    try:
        numero1 =input('Insira o primeiro numero: ')
        numero2 =input('Insira o segundo numero: ')
        
        numero1 = float(numero1)
        numero2 = float(numero2)
        

        while True:
            operador = input('Insira um operador: ')

            if operador == '+':
                print(numero1 + numero2)
                break
            elif operador == '-':
                print(numero1 - numero2)
                break
            elif operador == '/':
                print(numero1 / numero2)
                break
            elif operador == '*':
                print(numero1 * numero2)
                break
            else:
                print('Digite um operador valido')
                
    #########
        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break
    except:
        print('O numero digitado não era valido')