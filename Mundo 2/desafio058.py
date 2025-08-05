# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
import time
total = 1
computador = random.randint(1,10)
escolha = int(input('Digite o número que o computador pensou: '))
while escolha != computador:
    print('Pensando...')
    time.sleep(1)
    escolha = int(input('Incorreta! Escolha outro número: '))
    total += 1 
print(f'Acertou! O total de tentativas foi de {total}')
