# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro valor é maior')
elif n1 < n2:
    print('O segundo número é maior')
else:
    print('Não existe valor maior, os dois são iguais')
