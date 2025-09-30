'''
rotina -> coisa que vc faz constantemente 
no python -> print(), input(), len(), int()... build in function
def mostralinha()
    print('-='*30)

'''

'''def titulo(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))


titulo('   Curso em vídeo  ')
titulo('    python é muito bom!')'''
'''
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma A + B = {s}')
'''

'''
# Programa principal
soma(4,5)
soma(a= 4, b= 5)
# a =4 
# b = 5
# s = a+b
# print(s)

soma(8, 9)
# a = 8 
# b = 9
# s = a+b
# print(s)

soma(2,1)
# a = 1
# b = 2
# print(s)
soma(3, 9)'''


'''
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
    for v in num:
        print(v, end = ' ')
    print('FIM!')

contador(5,2,54,23,42)
contador(5,2,3,4,1,)
'''

'''
lst = [7,2,5,0,4]
outralst = [1,5,23,56,3]

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos +=1
    print(lista)

dobra(lst)
dobra(outralst)'''