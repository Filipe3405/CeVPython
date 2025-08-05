#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 > n3 or n1 > n3 > n2:
    if n2 > n3:
          print(f'o maior número é {n1} e o menor é {n3}')
    else:
     print(f'o maior número foi {n1} e o menor foi {n2}')
if n2 > n1 > n3 or n2 > n3 > n1:
    if n1 > n3:
          print(f'o maior número é {n2} e o menor é {n3}')
    else:
     print(f'o maior número foi {n2} e o menor foi {n1}')
if n3 > n2 > n1 or n3 > n1 > n2:
    if n2 > n1:
          print(f'o maior número é {n3} e o menor é {n1}')
    else:
     print(f'o maior número foi {n3} e o menor foi {n2}')
