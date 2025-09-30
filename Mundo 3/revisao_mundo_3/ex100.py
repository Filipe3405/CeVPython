'''Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocalos dentro da lista e a segunda função vai mostar a soma entre todos os valores pares sorteados pela função anterior'''

def sorteia():
    import random
    numeros = [random.randint(0,10),
               random.randint(0,10),
               random.randint(0,10),
               random.randint(0,10),
               random.randint(0,10),]
    return(numeros)


def SomaPar(par):
    total_par = 0
    for i in par:
        if i % 2 == 0:
            total_par += i
    print(f'A soma dos valores pares da lista {par} é {total_par}')

SomaPar(sorteia())