'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
cont = 'S'
while cont == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    cont = input('Você deseja adiconar outro número? [S/N]')[0].upper()
# A
print(f'Foram digitados {len(lista)} números')

#B
lista_cres = lista.sort()
print(f'A lista de forma crescente é {lista}')
lista_dec = lista.sort(reverse = True)
print(f'A lista de forma decrescente é {lista}')

# C
if 5 in lista:
    print('O cinco foi está na lista')
else:
    print('O cinco não está na lista')