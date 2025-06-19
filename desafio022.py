# Recebendo o nome da pessoa
nome = input('Digite o seu nome: ')
# Deixando o nome totalmente maiúsuclo
print(f'Seu nome em maiúsculo: {nome.upper()}')
# Deixando o nome totalmente minúsculo
print(f'Seu nome em minúsculo: {nome.lower()}')
# Tirando os espaços dos nomes
nomeesp = nome.replace(' ','')
# Contando a quantidade de caracteres sem os espaços
print(f'A quantidade de letras em seu nome é de: {len(nomeesp)}')
# Dividindo o nome
firstname = nome.split()
# Apresentando o primeiro nome
print(f'O seu primeiro nome é: {firstname[0]}')
