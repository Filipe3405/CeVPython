def aumentar(valor = 0,taxa = 0, form = False):
    if form:
        return moeda(valor + (valor * (taxa/100)))
    else:
        return valor + (valor * (taxa/100))


def diminuir(valor = 0, taxa = 0, form = False):
    if form:
        return moeda(valor - (valor * (taxa/100)))
    
    else:
        return valor - (valor * (taxa/100))


def dobro(valor = 0, form = False):
    if form:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor = 0, form = False):
    if form:
        return moeda(valor / 2)
    else:
        return valor / 2

def moeda(valor = 0,moed = 'R$', form = False):
    valor = (f'{moed} {valor:>2.2f}'.replace('.',','))
    return valor

def resumo(valor):
    print('-'*30)
    print(f'        RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço Analisado: {moeda(valor)}')
    print(f'Dobro do preço: {dobro(valor, True)}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'20% de aumento: {aumentar(valor,20, True)}')
    print(f'12% de redução: {diminuir(valor,12,True)}')
    print('-'*30)