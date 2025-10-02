'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
par = []
impar = []
cont = 'S'
while cont == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont = input('Você deseja adiconar outro número? [S/N]')[0].upper()
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(lista)
print(par)
print(impar)