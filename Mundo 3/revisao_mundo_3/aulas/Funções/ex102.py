'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show = True):
    f = 1
    for c in range(1, num+1, 1):
        f *= c
        if show == False and c == num:
            print(f'O fatoial de {num} é: {f}')  
        elif show == True:
            print(f, end = ' ')

        
            
fatorial(5, True)
fatorial(6, False)
fatorial(4, True)
