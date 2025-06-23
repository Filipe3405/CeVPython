# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time
print('==== Pedra Papel ou Tesoura ====')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogo = int(input('Escolha a sua jogada: '))
print('PEDRA!')
time.sleep(1)
print('PAPEL!')
time.sleep(1)
print('E TESOURA!')
time.sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
game = random.choice(lista)
if jogo == 1 and game == 'PEDRA':
    print(f'Você jogou PEDRA e a máquina jogou {game}. EMPATE!')
elif jogo == 1 and game == 'PAPEL':
    print(f'Você jogou PEDRA e a máquina jogou {game}. DERROTA!')
elif jogo ==1 and game =='TESOURA':
    print(f'Você jogou PEDRA e a máquina jogou {game}. VITÓRIA!')
elif jogo == 2 and game == 'PEDRA':
    print(f'Você jogou PAPEL e a máquina jogou {game}. VITÓRIA!')
elif jogo == 2 and game == 'PAPEL':
    print(f'Você jogou PAPEL e a máquina jogou {game}. EMPATE!')
elif jogo == 2 and game =='TESOURA':
    print(f'Você jogou PAPEL e a máquina jogou {game}. DERROTA!')
if jogo == 3 and game == 'PEDRA':
    print(f'Você jogou TESOURA e a máquina jogou {game}. DERROTA!')
elif jogo == 3 and game == 'PAPEL':
    print(f'Você jogou TESOURA e a máquina jogou {game}. VITÓRIA!')
elif jogo == 3 and game =='TESOURA':
    print(f'Você jogou TESOURA e a máquina jogou {game}. EMPATE!')


