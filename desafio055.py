# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 1000
for c in range(1,6):
    peso = int(input('Digite seu peso:'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso da lista é {maior}kg')
print(f'O menor peso da lista é {menor}kg')
