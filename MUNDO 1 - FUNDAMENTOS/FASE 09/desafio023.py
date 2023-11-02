# fazer um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c =  num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#n = str(num)
'''print('Analisando o número {}'.format())
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''