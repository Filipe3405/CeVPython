'''Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.'''

def escreva(txt):
    print('~'* len(txt))
    print(txt)
    print('~'*len(txt))


escreva('Olá, Mundo!')
escreva('   Gustavo Guanabara   ')
escreva('   Curso de Python no YouTube  ')
escreva(' CeV ')