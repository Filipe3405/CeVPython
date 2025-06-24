# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
from datetime import date
yr = date.today().year
nov = 0
idade = 0
old = 0
older = ''
for c in range (1,5):
    print(f'====== {c}º Pessoa ======')
    name = input('Digite seu nome: ').title().strip()
    sex = input('Sexo [H/M]: ').upper()
    nasc = int(input('Digite seu ano de nascimento: '))
    age = yr-nasc
    idade = idade + age
    if age < 20 and sex =='M':
        nov += 1
    if age > old and sex =='H':
        old = age
        older = name
print(f'A idade média do grupo é de {idade/4}, o homem mais velho é {older} e temos {nov} mulheres com menos de 20 anos.')
    
