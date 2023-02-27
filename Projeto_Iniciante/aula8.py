from datetime import date

nome = 'Felipe'
sobrenome = 'Motta'
idade = 23
anoNascimento = date.today().year - idade
maior_de_idade = idade >= 18
alturaMetros = 1.87
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', anoNascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', alturaMetros)

# def DescobrirAnoNascimento(date(aniversario)):
#     if(aniversario < date.today):
#         return date.year - aniversario
