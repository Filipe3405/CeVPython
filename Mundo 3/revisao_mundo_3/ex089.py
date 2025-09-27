'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
relatorio = []
aluno = []
while True:
    nome = input('Aluno: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    relatorio.append(aluno[:])
    aluno.clear()
    cont = input('Você deseja adicionar outro aluno? ').upper()
    if cont == 'N':
        break

for alunos in relatorio:
    print(f' {alunos[0]} Média: {(alunos[1]+alunos[2])/2}')

pesquisa = input('Pesquise um aluno: ')
for c in relatorio:
    if c[0] == pesquisa:
        print(c)

#    print(f'Isso é c: {c}')
 #   for i in c:
  #      print(f'Isso é i: {i}')
#        if pesquisa == c[i]:
#            print(c)