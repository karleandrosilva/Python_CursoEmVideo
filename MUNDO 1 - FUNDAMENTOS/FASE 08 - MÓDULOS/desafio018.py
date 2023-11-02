# fazer um programa que que leia um ângulo qualquer e mostre na tela do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
coss = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))