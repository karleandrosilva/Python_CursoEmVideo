# Criar um algoritmo que leia um número e mostre o dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)
print('O número escolhido é: {} \nO dobro é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}.'.format(num, dobro, triplo, raizq))