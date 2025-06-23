# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número: '))
for c in range(0,11,1):
    print(f'{num} x {c} = {num*c}')
