'''
Modularização
    - Década de 60
    - Programas crescendo
    - Foco: dividir um programa grande
    - Foco: aumentar a legibilidade
    - Foco: facilitar a manutentação
'''


from uteis import numeros
# Programa Principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'o fatorial do {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')