# fazer um programa que leia o sexo de uma pessoa, mas só aceita os valores 'm' ou 'f'. Caso esteja errado peça para digitar novamente.

sexo =  None # ou 0
masculino = 'm'
feminino = 'f'
while sexo != masculino and feminino:
    sexo = str(input('Olá, informe seu sexo [M/F]: '))
    if sexo == 'm':
        print('Você é do sexo Masculino!')
    elif sexo == 'f':
        print('Você é do sexo Feminino!')
    elif sexo != 'm' and 'f':
        print('Digite novamente!')
