# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
qntd = 0
count=0
n = 0
print('-'*30,'Máquina de somar','-'*30)
print('Obs: caso queira sair digite 999')
while n != 999:
    count += 1
    n = int(input('Digite um número: '))
    qntd += n
qntd = qntd -999
count = count-1
print(f'Foram digitados {count-1} números e a soma deles é de {qntd-999}')
