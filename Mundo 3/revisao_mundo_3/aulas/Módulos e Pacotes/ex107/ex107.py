import moedas
p = float(input('Digite o preço: R$ '))
print(f'Formatado {moedas.moeda(p)}')
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))} R$')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))} R$')
print(f'Aumentado 10%, temos {moedas.moeda(moedas.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(p,13))}')
