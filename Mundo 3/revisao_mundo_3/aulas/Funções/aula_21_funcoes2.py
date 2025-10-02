'''
* interactive help
* docstrings
* argumentos opicionais
* escopo de variáveis
* retorno de resultados
'''
#help(print)
#print(input.__doc__)

'''docstrings'''
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param:p passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!')


# contador(2,10,2)

'''def somar(a = 0,b = 0, c = 0):
    """
    Função com o objetivo de somar até 3 número, quando o valor do parâmetro não for definito, assume o valor 0
    """
    s = a + b +c
    print(f'A soma vale {s}')

somar(b = 4, c = 2)'''
'''
# Escopo de variáveis
def teste():
    x = 8  # Escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, o x vale {x}')
    
#Programa principal
n = 2  # Escopo global
teste()
print(f'No programa principal n vale {n}')
print(f'No programa principal x vale {x}')
'''

'''def teste(b):
    global a 
    a= 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')'''

# # Return
# def somar(a = 0,b = 0, c = 0):
#     """
#     Função com o objetivo de somar até 3 número, quando o valor do parâmetro não for definito, assume o valor 0
#     """
#     s = a + b +c
#     return(s)

# r1 = somar(5,2,3)
# r2 = somar(4)
# print(somar(3,6))
# print(f'Meus cálculos deram: {r1} e {r2}')

def fatorial(num =1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
