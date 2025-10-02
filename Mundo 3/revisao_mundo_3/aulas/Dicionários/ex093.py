'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
total = 0
partida = 1
jogador = {
    'jogador': input('Nome do jogador: ')
}
gols = {}
jogador['partidas'] = int(input(f'Quantas partidas o {jogador["jogador"]} jogou? '))
gols = []
for c in range(0, jogador['partidas']):
    gol = int(input(f'Quantos gols o {jogador["jogador"]} fez na partida {c}?'))
    total += gol
    gols.append(gol)

jogador['gols'] = gols
jogador['Total'] = total

print('-='*30)
print(jogador)
print('-='*30)


for k, v in jogador.items():
    print(f' - O campo: {k} tem o valor {v}')
print('-='*30)


print(f'O jogador {jogador["jogador"]} jogou {jogador["partidas"]} partidas.')
for c in jogador['gols']:
    print(f'        => Na {partida}ª partida, fez {c} gols.')
    partida += 1