'''Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area():
    a = float(input('Largura (m): '))
    b = float(input('Altura (m): '))
    area = a * b
    print(f'A área do terreno de {a}x{b} é de {area} m²')


def linha(msg):
    print('-='*30)
    print(msg)
    print('-='*30)

linha('Controle de Terrenos')
area()

