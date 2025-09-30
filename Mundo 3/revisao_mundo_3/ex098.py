'''faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim, passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1. b) de 10 até 0 de 2 em 2. c) uma contagem personalizada'''
import time
def contador(i, f, p):
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if p < 0:
        p *= -1
    if i < f:
        while i <= f:
            print(i, end=', ') 
            i = i + p
        print('Fim!')
        print('-='*30)
    elif i > f:
        while i >= f:
            print(i, end = ', ')
            i -= p
        print('Fim!')
        print('-='*30)    


contador(1,10,1)


contador(10,0,2)

print('Contagem personalziada: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
