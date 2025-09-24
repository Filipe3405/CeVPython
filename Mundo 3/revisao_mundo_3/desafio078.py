'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
num = []
max = 0
min = 1000000
for c in range(0,5):
    numero = int(input('Digite um número: '))
    num.append(numero)
    if numero >= max:
        max = numero
    elif numero < min:
        min = numero
print(f'O maior valor digitado foi: {max}')
print(f'o  menor valor digitado foi: {min}')
print(num)