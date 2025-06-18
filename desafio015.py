dias = int(input("Por quantos dias o carro será alugado?: "))
kms = float(input('Quantos kms serão andados?: '))
aluguel = dias * 60 + kms * 0.15
print(f'O valor total do aluguel será R${aluguel:.2f}')
