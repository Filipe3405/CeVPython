#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Computador "pensando" em um número
import random
num = random.randrange(0,5)
# Jogador escolhendo um número
jog = int(input("Digite um número: "))
# Comparando os números do computador com o do jogador
if jog == num:
    print('você acertou! :D')
else:
    print(f'Você errou! Eu pensei no número {num}:(')
