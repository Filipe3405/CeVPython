#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite seu salário: R$'))
if sal > 1250.00:
    print(f'Como seu salário é {sal}, o seu aumento será de 10% e ficará R${sal*1.1}')
else:
    print(f'Como o seu salário é {sal}, o aumento será de 15% e ficará R${sal*1.15}')
