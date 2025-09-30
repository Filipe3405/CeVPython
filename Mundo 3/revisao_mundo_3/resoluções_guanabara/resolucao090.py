aluno = dict()
aluno['Nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'aprovado'
elif 5 <= aluno['média'] <= 7:
    aluno['Situação'] = 'Em recuperação.'
else:
    aluno['Situação'] = 'Reprovado'

print('=-'*30)
for k, v in aluno.items():
    print(f'    - {k} é igual {v}')