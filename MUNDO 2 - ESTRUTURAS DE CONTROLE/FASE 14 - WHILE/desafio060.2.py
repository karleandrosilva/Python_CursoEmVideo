# EM FOR

num = int(input('Informe um número: '))
print('Calculando {}! = '.format(num), end='')
fcont = num
f = 1
for fcont in range(num,0,-1):
    print(fcont,end='')
    print(' x ' if fcont > 1 else ' = ', end='')
    f = f * fcont
print('{}'.format(f))
