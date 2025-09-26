'''
dados = list()
pessoas = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) # Pedro
print(dados[1]) # 25
pessoas.append(dados[:])
print(pessoas)
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(dados)
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]
'''
'''teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)'''

'''galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 65], ['Maria', 13]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''
galera = list()
dado = list()
total_maior = 0
total_menor = 0 
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor += 1
print(f'Temos {total_maior} maiores de idade e {total_menor} menores.')