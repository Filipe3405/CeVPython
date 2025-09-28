'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = dict()
jogadores = []
gols = []

while True:
    jogador['Nome'] = input('Nome: ').upper()
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(0,partidas):
        gol = int(input(f'Quantidade de Gols na partida {c}: '))
        gols.append(gol)
    jogador['gols'] = gols[:]
    gols.clear()
    jogadores.append(jogador.copy())
    cont = input('Você deseja adicionar outro jogador? [S/N]').upper()
    if cont != 'S':
        break

procura = input('Procure um jogador: ').upper()
for c in jogadores:
    if c['Nome'] == procura:
        print(c)