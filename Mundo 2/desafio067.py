# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
num = int(input('Digite um número: '))
x = 1
while True:
    if num < 0:
        break
    while x <=10:
        print(f'{num} x {x} = {num * x}')
        x +=1
    break
print('Fim')        
