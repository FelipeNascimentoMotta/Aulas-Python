primeiroValor = input('Digite o valor: ')
segundoValor = input('Digite outro valor: ')

if primeiroValor > segundoValor:
    print(f'O primeiro valor = {primeiroValor} é maior que o segundo valor = {segundoValor}')
elif segundoValor > primeiroValor:
    print(f'O segundo valor = {segundoValor} é maior que o primeiro valor = {primeiroValor}')
elif primeiroValor == segundoValor:
    print(f'Os valores são iguais {primeiroValor} e { segundoValor}')
else:
    print(f'O python não conseguiu comparar os valores {primeiroValor} e {segundoValor}')