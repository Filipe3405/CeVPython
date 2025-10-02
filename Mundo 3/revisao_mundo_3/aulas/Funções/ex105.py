'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas – A maior nota – A menor nota – A média da turma– A situação (opcional)'''

def notas(*num, sit = False):
    notas = dict()
    cont = maior = total = 0
    menor = 999999
    for i in num:
        if i > maior:
            maior = i
            total += i
        elif i < menor:
            menor = i
            total += i
        cont += 1
    media = total/cont
    notas['total'] = cont
    notas['maior'] = maior
    notas['menor'] = menor
    notas['media'] = media
    if sit:
        if media < 5:
            notas['situação'] = 'Reprovado'
        elif 5 <= media < 7:
            notas['situação'] = 'Em recupeação'
        elif media >= 7:
            notas['situação'] = 'Aprovado'
    return notas

resp =notas(4.5,10,6.5,4,7.5,2.4,10, sit= True)
print(resp)
