# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
if atual - ano == 18:
    print('É hora de se alistar: https://alistamento.eb.mil.br/alistamento')
elif atual - ano < 18:
    print(f'Você é jovem demais para se alistar, ainda faltam {18 - (atual - ano)} anos para você se alistar')
else:
     print(f'Você já se alistou ou já deveria ter se alistado. Já se passaram {(atual-ano)-18} anos do seu alistamento')
