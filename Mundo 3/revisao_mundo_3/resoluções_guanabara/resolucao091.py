import random
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {'jogador1': random.randint(1,6),
        'jogador2': random.randint(1,6),
        'jogador3': random.randint(1,6),
        'jogador4': random.randint(1,6)}

print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('== Ranking dos jogadores ==')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True)
for k,v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)