#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print(f'A sua velocidade excedeu o limite da pista em {vel-80}km/h e você foi multado em R${(vel-80)*7}')
else:
    print('Você não foi multado')
