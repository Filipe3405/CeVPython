# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operacao = 0
while operacao != 5:
    print('-------------------------------')
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    print('-------------------------------')
    operacao = int(input('Digite a operação desejada: '))
    print('-------------------------------')
    if operacao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif operacao == 2:
        print(f'A multiplicação entre {n1} e {n2} vale {n1*n2}')
    elif operacao == 3:
        if n1>n2:
            print(f'O maior valor é {n1}')
        else:
            print(f'O maior valor é {n2}')
    elif operacao == 4:
        n1 = int(input('Digite um novo valor para n1: '))
        n2 = int(input('Digite um novo valor para n2: '))
print('Fim do programa.')
