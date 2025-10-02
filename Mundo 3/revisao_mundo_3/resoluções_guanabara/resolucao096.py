def area(largura, comprimento):
    area = comprimento * largura
    print(f'A área de {comprimento} * {largura} = {area:3f} m²')


print(' Controle de Terrenos    ')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)