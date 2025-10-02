'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random
maior = 0
jogador_maior = ''

jogos = {'Jogador 1': random.randint(1,6), 'Jogador 2': random.randint(1,6), 'Jogador 3': random.randint(1,6), 'Jogador 4': random.randint(1,6)}

for k, v in jogos.items(): 
    if v > maior:
        maior = v
        jogador_maior = k

print(f'O maior valor foi {jogador_maior} com o valor {maior}')
print(jogos)

