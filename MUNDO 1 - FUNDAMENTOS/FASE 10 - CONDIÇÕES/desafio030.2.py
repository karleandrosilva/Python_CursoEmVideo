print('---DESAFIO 030---')
print('-----------------')
n = int(input('DIGITE UM NÚMERO: '))

# divisão por dois
par = n % 2
# se o resto da divisão for 0 é par

if par == 0:
    print('O', n, 'É PAR!')

# se não é impar
else:
    print('O', n, 'É IMPAR!')