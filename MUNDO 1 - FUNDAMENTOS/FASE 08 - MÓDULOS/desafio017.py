# CATETO E HIPOTENUSA

# fazer um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triãngulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacentes: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adiacentes: '))
#calculohi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(calculohi))