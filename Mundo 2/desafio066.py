#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
total = c = soma = 0
while True:
    c = int(input('Digite um número: '))
    if c == 999:
        break
    total += 1
    soma += c

print('Fim!')
print(f'Foram digitados {total} números que somados dão {soma}')
