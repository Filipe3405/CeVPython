# Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for c in range(1,51,1):
    if c % 2 == 0:
        print(c, end=' ')
