# Fazer um programa que pergunte quantos dias foi alugado o carro e quantos km rodados, e calcule quanto pagará, sabendo que cada dia alugado é 60 reais, e cada km rodado é 0.15 centavos.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))