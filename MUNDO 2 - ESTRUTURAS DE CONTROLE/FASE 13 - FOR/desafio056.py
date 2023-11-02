# desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa.
somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = 0
totalmulher = 0

for p in range(1,5):
    print('--- {}ª PESSOA ---'.format(p))
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totalmulher += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))

print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeh, nomevelho))

print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalmulher))