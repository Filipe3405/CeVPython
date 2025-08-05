# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1= int(input('Digite o primeiro termo da progressão:'))
r = int(input('Digite a razão da progressão: '))
p = 1
while p < 11:
    print(a1+(p-1)*r, end=' ')
    p += 1
print('-> Fim do programa!')
