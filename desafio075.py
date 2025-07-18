# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
pares = nove  = 0

# Obtendo os  4 valores
n = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

# Quantas vezes o 9 apareceu
print(f'O valor nove apareceu {n.count(9)} vezes')
# Em que posição temos o primeiro 3
if 3 in n:
    print(f'O valor três apareceu na posição {n.index(3)}')
else:
    print('O três não apareceu na sequência')
# Quais foram os pares
for num in n:
    if num % 2 == 0:
        print(f'{num}', end=' ')


# Nesse exercício, com auxílio da resolução, apredi a usar o count e o index para descobrir quantas vezes e em qual posição algum número apareceu.
