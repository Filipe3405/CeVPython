# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Tratando como string
num = (input('Digite um número entre 0 e 9999: '))
alg = (' '.join(num)).split()
print(f'unidade: {alg[3]}')
print(f'dezena: {alg[2]}')
print(f'centena: {alg[1]}')
print(f'milhar: {alg[0]}')
# Com as ferramentas atuais, o exercício embora dê erro foi executado da maneira esperada
# Resolução do Guanabara
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
