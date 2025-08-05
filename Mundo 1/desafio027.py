# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
nome = input('Digite seu nome completo: ')
nomelist = nome.split()
frstname = nomelist[0]
print(f'Primeiro nome: {frstname}')
print(f'Seu último nome: {nomelist[len(nomelist)-1]}')

