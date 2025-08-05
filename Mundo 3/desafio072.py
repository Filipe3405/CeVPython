#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis', 'Dezesete','Dezoito','Dezenove', 'Vinte')
while 0 <= x <=20:
    x = int(input('Digite um número entre 0 e 20: '))
    while x not in range(0,21):
         x = int(input('Digite um valor válido: '))
    print(extenso[x])
    cont = input('Você deseja continuar?[S/N]: ').upper().strip()
    if cont == 'N':
        break
print('Fim do programa.')
