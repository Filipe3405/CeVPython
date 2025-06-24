# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from datetime import date
ano_atual = date.today().year
mulher_menos_20 = 0
idade_total = 0
idade_mais_velho = 0
nome_mais_velho = ''
for pessoa in range (1,5):
    print(f'====== {pessoa}º Pessoa ======')
    nome = input('Digite seu nome: ').title().strip()
    sex = input('Sexo [H/M]: ').upper()
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - nasc
    idade_total = idade_total + idade
    if idade < 20 and sex =='M':
        mulher_menos_20 += 1
    if idade > idade_mais_velho and sex =='H':
        idade_mais_velho = idade
        nome_mais_velho = nome
print(f'A idade média do grupo é de {idade_total/4:.1f} anos')
if nome_mais_velho != '':
    print(f'O homem mais velho é {nome_mais_velho}')
else:
    print('Não há homens nesse grupo')
print(f'Temos {mulher_menos_20} mulheres com menos de 20 anos.')
    
