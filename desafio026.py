#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip()
x = frase.count('a')
y = frase.count('á')
z = frase.count('à')
w = frase.count('â')
print(f'A letra "a" aparece {x+y+z+w} vezes nessa frase')
print(f'A primeira letra "a" aparece na posição {frase.find('a')+1}')
print(f'A última letra "a" aparece na posição {frase.rfind('a')+1}')
