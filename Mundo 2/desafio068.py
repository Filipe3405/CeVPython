# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
import random
victory = True
count = 0
print('Par ou ímpar')
print('[1] ÍMPAR')
print('[2] PAR')
jogada = int(input('Escolha sua jogada:'))
while victory == True:
    jogador = int(input('Digite um número: '))
    comp = random.randint(0,5)
    num = jogador+comp
    if jogada == 1:
        if num % 2 == 0:
            print(f'{jogador}+{comp}={num} é um número par')
            break
        elif num % 2 != 0:
            print(f'{jogador}+{comp}={num} é um número ímpar')
            count += 1
            print('Vitória')
    elif jogada ==2:
            if num % 2 == 0:
                print(f'{jogador}+{comp}={num} é um número par')
                count += 1
                print('Vitória')
            elif num % 2 != 0:
                print(f'{jogador}+{comp}={num} é um número ímpar')
                break
print(f'Você ganhou {count} vezes')

# Onde melhorar?
# Possibilidade para alterar se quer par ou impar em cada jogada
