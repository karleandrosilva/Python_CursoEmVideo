# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Que ano quer analisar? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSESTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))