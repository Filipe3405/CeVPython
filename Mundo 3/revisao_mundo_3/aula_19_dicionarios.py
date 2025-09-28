'''
Dicionários
'''
'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
'''
'''dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
dados['sexo'] = 'M'
del dados['idade']
print(dados)
'''
'''starwars = {'título':'star wars', 'ano':1977, 'diretor':'George Lucas'}
avangers = {'título': 'Avangers', 'ano': 2012, 'diretor': 'Joss Whedon'}
matrix = {'título': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}'''
'''print(filme.values())
print(filme.keys())
print(filme.items())
print(filme)'''

'''for key, value in filme.items():
    print(f'O  {key} é {value}')
    '''
'''locadora = list()
locadora.append(starwars)
locadora.append(avangers)
locadora.append(matrix)
print(locadora[0]['ano'])'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas['nome'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'sao paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

'''estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa'))
    estado['silga'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k,v in e.items():
        print(f'{k} = {v}')'''