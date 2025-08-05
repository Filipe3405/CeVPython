# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

# Recebendo os números
lista = (int(input('Digite o 1º número: ')),int(input('Digite o 2º número: ')),
         int(input('Digite o 3º número: ')),int(input('Digite o 4º número: ')),
         int(input('Digite o 5º número: ')))

# Apresentando o maior valor e sua posição
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))+1}')

# Apresentando o menor valor e sua posição
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))+1}')
