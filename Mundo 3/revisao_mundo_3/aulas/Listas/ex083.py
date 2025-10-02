'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
cont = 0
expressao = input('Digite uma expressão: ')
for i in range(0,len(expressao)):
    if expressao[i] == '(' or expressao[i] == ')':
        cont += 1
if cont % 2 == 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')
