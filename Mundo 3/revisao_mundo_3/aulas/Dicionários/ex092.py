'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

pessoa = {'nome:': input('Nome: '), 'ano de nascimento': int(input('Ano de nascimento: ')), 'CTPS': int(input('carteira de trabalho: '))}
if pessoa['CTPS'] != 0:
    pessoa['salario'] = float(input('Salario:'))
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['aposentadoria'] = (pessoa['ano de contratação'] + 35)- 2000
pessoa['idade'] = 2025 - pessoa['ano de nascimento']

# print(pessoa)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')