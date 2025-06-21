# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota: '))
med = (n1+n2)/2
if med < 5:
    print(F'Média final: {med}. REPROVADO')
elif med > 7:
    print(f'Média final {med}. APROVADO')
else:
    print(f'Média final {med}. RECUPERAÇÃO')
