# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
total = 0
for _ in range(0,6):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
        total = total + num
print(total)
