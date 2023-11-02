# fazer um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele aida vai ser alistar ao serviço militar se é a hora de se alistar ou se já passou do tempo do alistamento.

from datetime import date

ano_atual = date.today().year

print('---ALISTAMENTO---')
print('-----------------')

sexo = int(input('''Informe o seu sexo 
[ 1 ] MASCULINO
[ 2 ] FEMININO: ''')) 

if sexo == 1:
    ano_nasc = int(input('Digite o ano do seu nascimento: '))

    idade = ano_atual - ano_nasc 

    print('Quem nasceu em {} tem {} anos de idade.'.format(ano_nasc,idade))

    if idade == 18:
        print('Já está na hora de se alistar, não perca o prazo!')
    elif idade < 18:
        print('Você ainda vai se alistar, não perca o prazo!')
        saldo = 18 - idade
        print('Falta ainda {} anos para seu alistamento.'.format(saldo))
        ano = ano_atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        print('Já passou o prazo de se alistar!')
        saldo = idade - 18
        print('{} anos que passou do seu alistamento.'.format(saldo))
        ano2 = ano_atual - saldo
        print('Seu alistamento foi em {}'.format(ano2))
elif sexo == 2:
    print('VOCE NÃO PRECISA FAZER O ALISTAMENTO!')
else:
    print('COMANDO INVÁLIDO, TENTE NOVAMENTE!')



