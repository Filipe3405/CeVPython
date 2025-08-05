# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes 
l1 = int(input('Digite o primeiro lado do triângulo: '))
l2 = int(input('Digite o segundo lado do triângulo: '))
l3 = int(input('Digite o terceiro lado do triângulo: '))
if l1 == l2 == l3:
    print('O triângulo é equilátero')
elif l1 != l2 != l3:
    print('O triângulo é escaleno')
else:
    print('O triângulo é isósceles')
