'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = {}
contatos = []
mulheres = []
seniors = []
total = 0
idade = 0
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Sexo'] = input('Sexo: [M/F] ').upper()
    pessoa['Idade'] = int(input('Idade: '))

    total += 1
    idade += pessoa['Idade']

    contatos.append(pessoa.copy())

    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa.copy())
    
    cont = input('Quer adicionar outro contato? ').upper()
    if cont == 'N':
        break
media = idade/total
for c in contatos:
    if c['Idade'] > media:
        seniors.append(c.copy())
print(contatos)
print(f' Foram adicioandos {total} contatos')
print(f' A média de idade dos contatos é de {idade/total}')
print(mulheres)
print(seniors)