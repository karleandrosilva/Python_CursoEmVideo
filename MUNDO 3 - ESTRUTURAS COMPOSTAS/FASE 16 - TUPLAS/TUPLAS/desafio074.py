# programa que gera cinco números aleatórios e coloca em uma tupla e mostra a listagem de números gerados e também indica o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: ', end='')

for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')