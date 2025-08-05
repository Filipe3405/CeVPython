# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 
total = mais_mil = 0
menor_valor = 100000
mais_barato =''
while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    if valor > 1000:
        mais_mil = mais_mil + 1
    total = total+valor
    if valor < menor_valor:
        menor_valor = valor
        mais_barato = nome
    continuar = input('Você deseja continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break
print(f'O total das compras foi {total}, {mais_mil} produtos custam mais de R$1000 e {mais_barato} foi o produto mais barato')
