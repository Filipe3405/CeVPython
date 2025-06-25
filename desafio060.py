# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
import math
num = int(input('Digite um número: '))
x = math.factorial(num)
print(f'{num}!= {num} x', end=' ')
while num != 1:
    num = num-1
    if num == 1:
        print(f'{num} =', end=' ')
    else:
        print(f'{num} x', end=' ')
print(x)
