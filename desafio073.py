# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense -> mirassol.
times = ('Cruzeiro', 'Flamengo', 'Bragantino', 'Bahia', 'Palmeiras', 'Botafogo', 'Fluminense', 'Atlético MG','Corinthians', 'Ceará SC', 'Mirassol', 'Grêmio', 'Santos', 'Internacional', 'Vasco da Gama', 'São Paulo', 'EC Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')
#Os 5 primeiros times
print(times[0:5])
# Os últimos 4 colocados
print(times[16:20])
# Em ordem alfabética
print(sorted(times))
#Posição do Mirassol
for pos, time in enumerate(times):
    if time == 'Mirassol':
         print(f'{time} na posição {pos}')
