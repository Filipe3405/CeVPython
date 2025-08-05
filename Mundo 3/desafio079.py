# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        num = int(input('Número já adicionado, digite outro:'))
        lista.append(num)
    else:
        lista.append(num)
    cont = input('Você deseja continuar?[S/N]: ').upper().strip()
    if cont == 'N':
        break
    elif cont!= 'S':
        cont = input('Digite uma opção válida [S/N]: ')
print(sorted(lista))
        
