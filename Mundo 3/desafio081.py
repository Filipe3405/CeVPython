# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
cinco = False
while True:
    lista.append(int(input('Digite um número: ')))
    cont = input('Você deseja adicionar outro número?[S/N]: ').upper()[0]
    if cont == 'N':
        break
    while cont not in 'NS':
        cont = input('Digite um opção válida[S/N]: ').upper()[0]
if 5 in lista:
    cinco = True
print(f'Foram digitados {len(lista)} números')
lista_ordenada = sorted(lista, reverse = True)
print(lista_ordenada)
print(f'O número cinco foi digitado?: {cinco}')
