# fazer um programa que leia um número qualquer e mostre qualquer e mostre o seu fatorial.

num = int(input('Informe um número: '))
print('Calculando {}! = '.format(num), end='')
cont = num
f = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    #if 
        #if cont > 1:
            #print(' x ', end='')
        #else:
            #print(' = ', end='')
    f = f * cont
    cont = cont -  1
print(f)