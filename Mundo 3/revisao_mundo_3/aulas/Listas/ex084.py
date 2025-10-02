'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.'''
dados = list()
nome_peso = list()
total_pessoas = 0
peso_total = 0 
pesados = list()
leves = list ()

while True:
    dados.append(input('Nome:'))
    dados.append(int(input('Peso: ')))
    nome_peso.append(dados[:])
    cont = input('Você deseja cadastrar outra pessoa? [S/N]').upper()
    total_pessoas += 1
    dados.clear()

    if cont == 'N':
        break

print(f'Foram cadastradas {total_pessoas} pessoas')

for p in nome_peso:
    peso_total += p[1]

media = peso_total/total_pessoas

print(media)
for i in nome_peso:
    if i[1] > media:
        pesados.append(i[0])
for i in nome_peso:
    if i[1] < media:
        leves.append(i[0])

for _ in pesados:
    print('Os mais pesados são:', end = '')
    print(pesados)

for _ in leves:
    print('Os mais leves são:', end = '')
    print(leves)
