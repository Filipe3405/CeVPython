'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
valores = list()

for i in range(1,8):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        valores.append(numero)
    else:
        valores.insert(0, numero)
print(f'Pares:', end=' ')    
valores.sort()
for num in valores :
    if num % 2 == 0:
        print(f'{num}', end=' ')
print('')
print('Impares:', end=' ')
for num in valores:  
    if num % 2 != 0:
        print(f'{num}', end=' ')