'''Faça um programa que leia nome e média de um aluno guardando também a situação em um dicionário. no final, mostre o conteúdo da estrutura na tela'''
nota = {'Nome': input('Nome: '), 'Nota': int(input(f'Media: '))}

if nota['Nota'] > 5:
    nota['Situação'] = 'Aprovado'
 
else:

    nota['Situação'] = 'Reprovado'

for k, v in nota.items():
    print(f'{k} é igual a {v}')