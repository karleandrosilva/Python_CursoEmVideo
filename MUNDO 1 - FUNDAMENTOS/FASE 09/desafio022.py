# criar um programa que leia o nome completo de uma pessoa e mostre: 

nome = str(input('Digite seu nome completo: ')).strip()

# maiusculo
print('Seu nome todo em maiscúlo: ',nome.upper())

# minusculo
print('Seu nome todo em minúsculo: ',nome.lower())

# quantas letras tem ao todo
print('Seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))

# quantas letras tem o primeiro nome
separa = nome.split()

print('Seu primeiro nome é {} e tem: {} letras'.format(separa[0], len(separa[0])))

#print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))