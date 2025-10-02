from time import sleep
def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end =' ', flush= True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print()
    print('-'*40)
    print(f'Foram analisados {cont} valores ao todo.')
    print(f'O maior valor analisado foi {maior}')
    print('-'*40)
# Programa principal


maior(2,9,4,5,7,1)