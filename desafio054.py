# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
maior = 0.
menor = 0
for c in range(0,7):
    nasc = int(input('Digite o seu ano de nascimento: '))
    if ano - nasc >= 18:
        print('Maior')
        maior += 1
    else:
        print('Menor')
        menor += 1
print(f'O número de menores é {menor} e de maiores é de {maior}')
