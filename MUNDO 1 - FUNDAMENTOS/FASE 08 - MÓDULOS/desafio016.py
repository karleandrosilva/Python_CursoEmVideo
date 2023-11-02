# Crie um programa que leia um número real qualquer e mostre na tela a sua porçâo inteira.

'''num = float(input('Digite ym valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''


from math import trunc

num = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))


