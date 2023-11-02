# fazer um programa que leia o ano de nascimento de um atleta e mostre sua cateoria, de acordo com a idade.

from datetime import date

nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual- nasc 

if idade <= 9:
    print('Você tem {} anos, e sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, e sua categoria é INFATIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, e sua categoria é JUNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, e sua categoria é SENIOR!'.format(idade))
else:
    print('Você tem {} anos, e sua categoria é MASTER!'.format(idade))