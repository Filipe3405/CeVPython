# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite um frase:')).upper()
fras1 = frase.strip().replace(' ','')
x = ''.join(reversed(fras1))
print(x)
if x == fras1:
    print('Palíndromo')
