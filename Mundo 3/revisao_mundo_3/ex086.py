'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[],[],[],[],[],[],[],[],[]]
for i in range(0,9):
    elemento = int(input(f'Digite o {i+1}º elemento: '))
    matriz[i].append(elemento)
#print(matriz)
print('Matriz')
for c in range(0,3):
    print(matriz[c], end=' ')
print('')
for d in range(3,6):
    print(matriz[d], end=' ')
print('')
for f in range(6,9):
    print(matriz[f], end=' ')
print('')