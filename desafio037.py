#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 
print('Sistemas numéricos')
num = int(input('Digite um número: '))
print('[1] Sistema Binário')
print('[2] Sistema octal')
print('[3] Sistema hexadecimal')
sis = int(input('Digite qual seu sistema de escolha: '))
if sis == 1:
    print(f'O valor {num} na base binária é de:{bin(num)[2:]}')
elif sis ==2:
    print(f'O valor {num} na base octal é de: {oct(num)[2:]}')
elif sis == 3:
    print(f'O valor {num} na base hexadecimal é de: {hex(num)[2:]}')
else:
  print('Escolha uma base válida!')
