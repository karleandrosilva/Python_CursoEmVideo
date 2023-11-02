# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(c, end=' - ')
print('\n\033[mO número {} foi divísivel {} vezes.'.format(num,total))
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO é PRIMO!')
