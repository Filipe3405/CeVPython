# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
x = random.randint(0,100)
y = random.randint(0,100)
z = random.randint(0,100)
a = random.randint(0,100)
b = random.randint(0,100)
tupla = (x,y,z,a,b)
tupla_ordenada = sorted(tupla)
print(f'A tupla aleatória é: {tupla}')
print(f'O menor número da tupla aleatória é: {tupla_ordenada[0]}')
print(f'O maior número da tupla aleatória é {tupla_ordenada[4]}')
