# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida 
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(altura**2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} - Abaixo do peso')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é de {imc:.2f} - Peso ideal')
elif 25 < imc < 30:
    print(f'Seu IMC é de {imc:.2f} - Sobrepeso')
elif 30 < imc < 40:
    print(f'Seu IMC é de {imc:.2f} - Obesidade')
else:
     print(f'Seu IMC é de {imc:.2f} - Obesidade Mórbida')
