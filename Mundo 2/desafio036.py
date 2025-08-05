#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite em quantos anos você deseja pagar: '))
prest = (casa / (anos*12))
print(f'A quantidade de parcelas será {prest}')
if prest <= salario * 0.3:
    print('Seu empréstimo foi aceito')
else:
    print('Seu empréstimo foi negado')
