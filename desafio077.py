# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista = ('Exercicio', 'Tabular', 'Naturalmente', 'Estamos', 'Maratonando', 'Probalidade')
for palavra in lista:
    print(palavra, end=' ')
    for vogal in palavra:
        if vogal in 'aeiouAEIOU':
            print(vogal, end='.')
    print('')
