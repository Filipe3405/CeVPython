'''comidas = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(comidas)
comidas[3] = 'Picolé'
print(comidas)
comidas.append('Cookie') # Adiciona elementos ao final da lista
comidas.insert(0, 'Cachorro Quente') # Adiciona elementos no local definido
print(comidas)


Formas para deletar elementos de uma lista
    del lanche[3]
    lanche.pop(3)
    lanche.remove('Pizza')

del comidas[3]
print(comidas)

if 'Suco' in comidas:
    comidas.remove('Suco')
print(comidas)

valores = list(range(4,11))
print(valores)

# sort -> ordena os elementos, se quiser reverter (reverse= True)
# len -> quantos valores tem na lista
'''
num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7)
num.sort(reverse = True)
num.insert(2, 0)
print(num)
num.pop(2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

for n in num:
    print(n, end=' ')