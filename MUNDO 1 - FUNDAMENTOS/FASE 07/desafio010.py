# Criar um programa que leia quarto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input('Quantos reais você tem na carteira: R$'))
dolar = 3.27

print('Você pode comprar U${:.2f} de dolares.'.format(money / dolar))