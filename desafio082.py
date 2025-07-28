# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número?: '))
    lista.append(num)
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num)
    cont = input('Você deseja continuar?[S/N]: ').upper()[0]
    while cont not in 'NS':
        cont = input('Digite uma opção válida: ')
    if cont == 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')
