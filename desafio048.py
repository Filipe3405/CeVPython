# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
total = 0
for c in range(3,501,3):
       total = total + c
print(total)
