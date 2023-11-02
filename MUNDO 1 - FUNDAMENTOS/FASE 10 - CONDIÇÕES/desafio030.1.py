# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))

# para saber se é par, primeiro descubra o valor por dois.
par = n % 2

# se o resto da divisão for 0 é par
if par == 0:
    print('O NÚMERO {} É PAR!'.format(n))

# se não, é impar
else:
    print('O NÚMERO {} É IMPAR!'.format(n))

