# deselvoler um programa que leia o comprimento de tres retas e diga ao usuario se ellas podem ou nao formar um triagulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMA UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO FORMA UM TRIÂNGULO!')