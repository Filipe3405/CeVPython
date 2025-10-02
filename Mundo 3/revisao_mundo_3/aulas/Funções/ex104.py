'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaint():
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
    return n
n = leiaint()
print(n)