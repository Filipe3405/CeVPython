def fatorial(n, show = False):
    '''
    -> calcula o fatorial de um número.
    :param n:O número a ser calculado.
    :param show: define se mostra ou não a conta.
    :return: O valor do fatorial de um numero n.
    '''
    f = 1
    for c in range (n,0,-1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end='')
            else:
                print(' =' , end='')
        f *= c
    return f


# Programa principal
print(fatorial(5,True))
help(fatorial)