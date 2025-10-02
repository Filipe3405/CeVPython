'''Crie um progrma que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto negado, opcional ou obrigatório'''

import datetime

def voto(nasc):
    idade = datetime.date.today().year - nasc
    if idade < 16:
        return(f'Com {idade} anos: VOTO NEGADO')
    elif 16<= idade <18 or idade >= 70:
        return(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    
nasci = int(input('Ano de nascimento: '))
print(voto(nasci))