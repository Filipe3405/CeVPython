#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dis = float(input('Digite a distância da viagem em km: '))
if dis <= 200:
    print(f' O preço de uma viagem de {dis}km é de R$ {dis * 0.5}')
else:
    print(f'O preço de uma viagem de {dis}km é de R${dis*0.45}')

