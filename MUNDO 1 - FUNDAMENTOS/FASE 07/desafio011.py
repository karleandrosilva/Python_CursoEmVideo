# Fazer um programa que leia a largura e a altura de uma parede em metros, e calcule a área e a quantdade de tinta.

larg = float(input('Qual é a largura da parede: '))
comp = float(input('E o comprimento: '))
area = larg * comp
ltinta = area / 2

print('A área é: {} metros\nQuantidade de tinta para pintar: {}litros'.format(area, ltinta))

