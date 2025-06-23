# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Digite A1: '))
r = int(input('Digite a razão da progressão: '))
for c in range(0,10):
    an = a1+(r*c)
    print(f'O A{c+1} vale: {an}')
