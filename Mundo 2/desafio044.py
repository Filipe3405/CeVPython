# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
valor = float(input('Digite o valor do produto: R$'))
print('Formas de pagamento')
print('[1] Á vista em dinheiro ou cheque: 10% de desconto')
print('[2] À vista no cartão: 5% de desconto')
print('[3] Em até duas vezes no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
forma = int(input('Escolha a forma de pagamento: '))
if forma == 1:
    print(f'O valor do produto na forma de pagamento {forma} é de R${valor*0.9}')
elif forma == 2:
    print(f'O valor do produto na forma de pagamento {forma} é de R${valor*0.95}')
elif forma ==3:
    print(f'O valor do produto na forma de pagamento {forma} é de R${valor} com parcelas de {valor/2}')
elif forma == 4:
    parc = int(input('Em quantas parcelas deseja pagar?: '))
    print(f'O valor do produto na forma de pagamento {forma} é de R${valor*1.2} com {parc} parcelas de R${(valor*1.2)/parc}')
else: 
    print('Opção inválida')
