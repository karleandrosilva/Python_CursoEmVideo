# fazer um programa que leia dois númeos inteiros e compare-os mostrando qual é o maior.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O {} é o maior valor.'.format(num1))

elif num2 > num1:
    print('O {} é o maior valor.'.format(num2))

else:
    print('Não existe valor maior, os dois são iguais.')