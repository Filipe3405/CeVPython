#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('Digite o nome da sua cidade: ').title()
city = cidade.split()
print('Santo' in city[0])
# Outra resolução com condicionais 
cidade = input('Digite o nome da sua cidade: ')
frstname = cidade.split()
if frstname[0] == 'Santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
