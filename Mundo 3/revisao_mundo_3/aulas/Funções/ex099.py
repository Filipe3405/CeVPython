'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar e dizer qual deles é o maior'''

def maior(*num):
    maior = 0
    for i in range(0, len(num)):
        if num[i] > maior:
            maior = num[i]
    print(f'O maior número digitado foi: {maior}')

maior(4, 5, 2, 3, 8)
maior(6,1,2,5,23,120)