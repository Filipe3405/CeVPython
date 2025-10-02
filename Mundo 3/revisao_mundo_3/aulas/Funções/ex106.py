'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''

def ajuda():
    while True:
        print('-'*20)
        msg = input(f'\033[0;30;41mDigite um comando: \033[m')
        print('-'*20)
        if msg == 'FIM':
            break
        print(f'\33[1;40;37m{msg.__doc__}\033[m')
ajuda()