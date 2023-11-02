# fazer um programa que mostre que tipo de triângulo pode ser formado.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \nPODEM FORMAR um triângulo!')
    if r1 == r2 and r2 == r3:
    #if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
    #elif r1 != r2 != r3 != r1:
       print('ESCALENO!') 
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima \nNÃO PODEM FORMAR um triãngulo!')

