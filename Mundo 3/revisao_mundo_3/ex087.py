'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.'''
matriz = [[],[],[],[],[],[],[],[],[]]
soma_par = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = -9999999999


for i in range(0,9):
    elemento = int(input(f'Digite o {i+1}º elemento: '))
    if 2 < i < 7:
        if elemento > maior_valor_segunda_linha:
            maior_valor_segunda_linha = elemento
        
    if elemento % 2 == 0:
        soma_par += elemento
    matriz[i].append(elemento)
    
    if i == 2 or i == 5 or i == 8:
        soma_terceira_coluna += elemento

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
print(f'A soma de todos os valores pares digitados foi: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')