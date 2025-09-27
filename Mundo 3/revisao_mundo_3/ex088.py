'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
qntd = int(input('Digite a quantidade de jogos: '))
jogos = []
for q in range(0, qntd):
    jogos.append([])

for jogo in jogos:
    for i in range(0,6):
        numero = random.randint(1,60)
        jogo.append(numero)
for c in range(0,qntd):
    print(f'O {c+1}º jogo será: {jogos[c]}')