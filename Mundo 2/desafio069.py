# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
continuar = 'S'
countidade = countmulher = counthomem = 0
while continuar == 'S':
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        countidade = countidade + 1
    sexo = input('Digite o sexo [M/F]').strip().upper()
    while True:
        if sexo in ['M','F']:
            break
        else:
            sexo = input('Digite um sexo válido [M/F]: ').strip().upper()
    if sexo == 'F' and idade < 20:
        countmulher = countmulher + 1
    elif sexo =='M':
        counthomem = counthomem + 1
    continuar = input('Você quer continuar? [S/N]').strip()[0].upper()
print(f'Foram cadastradas {countidade} pessoas com mais de 18 anos, {counthomem} homens e {countmulher} mulheres com menos de 20 anos')
