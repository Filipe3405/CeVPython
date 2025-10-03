def leiaint():
    n = input('Digite um número inteiro: ')
    try:
        n = int(n)
        return n
    except:
        while n.isdigit == False:
            n = input('\033[1;30;31mERRO: por favor, digite um número inteiro válido\033[0m')


def leiafloat():
    n = input('Digite um número real: ')
    try:
        n = float(n)
        return n
    except:
        return ('\033[1;30;31mO valor digitado não é um número real\033[0m')
print(f'O valor inteiro digitado foi {leiaint()} e o real foi {leiafloat()}')