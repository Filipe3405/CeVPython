# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. OK
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = []
dados = []
pesadas = []
leves = []
totalpessoas = pesototal = 0
# Obtendo dados de entrada
while True:
    print('-='*30)
    dados.append(input('Nome: ').title())
    totalpessoas += 1
    dados.append(int(input('Peso: ')))
    pesototal += dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = input('Você deseja continuar?[S/N]: ').upper()
    if cont == 'N':
        break
    while cont not in 'SN':
        cont = input('Digite uma opção válida! [S/N]: ').upper()
# Obtendo os valores extremos de máximo e mínimo
maior = max(peso[1] for peso in pessoas)
menor = min(peso[1]for peso in pessoas)
# Listando os extremos
for c in pessoas:
    if c[1] == maior:
        pesadas.append(c[0])
    elif c[1] == menor:
        leves.append(c[0])
# Apresentando os dados
print(f'Foram cadastradas {totalpessoas} pessoas')
print(f'As pessoas mais pesadas são: {pesadas}')
print(f'As pessoas mais leves são: {leves}')