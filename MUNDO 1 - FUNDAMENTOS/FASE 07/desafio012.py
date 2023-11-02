# Fazer um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Qual o preço do produto: '))
npreco = preco - (preco*5/100)

print('O produto custava R${:.2f}, na promoção de 5% de desconto vai custar R${:.2f}.'.format(preco, npreco))