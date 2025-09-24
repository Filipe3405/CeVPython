'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

# Criação das estruturas básicas Lista e Verificação
valores = []
cont = 'S'

# Primeiro número da lista, independente de qual for colocado, sempre estará disponível
valor_inicial = int(input('Digite um número: '))
valores.append(valor_inicial)
cont = input('Você deseja adiconar outro número?: [S/N]').upper()

# Estrutura de verificação de dados
while cont == 'S':
    numero = int(input('Digite um número: '))     
    if numero in valores:
        print('Esse número já existe!')
    else:
        valores.append(numero)
    cont = input('Você deseja adiconar outro número?: [S/N]').upper()
print(valores)