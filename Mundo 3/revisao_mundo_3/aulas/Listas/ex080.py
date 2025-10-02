''' 
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
valores = []
numero = int(input('Digite um número: '))
valores.append(numero)
for i in range(4):
    numero = int(input('Digite um número: '))
    if numero < valores[-1]:
        valores.append(numero)
    else:
        for c in range(0, len(valores)):
            if numero >= valores[c]:
                valores.insert(c, numero)
                break
print(valores)