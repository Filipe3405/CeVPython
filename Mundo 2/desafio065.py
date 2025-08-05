# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
quer = 'S'
maior = total =count = 0
menor = 100000
while quer in 'S':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    total += num
    count +=1
    quer = input('Você quer continuar?[S/N]: ').upper().strip()[0]
print(f'A média dos valores digitados é de {total/count:.2f}, o maior número foi {maior} e o menor foi {menor}')
