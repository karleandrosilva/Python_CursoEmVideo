# criar um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valoR: 999, que é a condição de parada. No final, mostre QUANTOS NÚMEROS foram digitados e quak foi a soma entre eles (desconsiderando o 999).
num = 0
cont = 0
soma = 0
num = int(input('Digite um número\n[999 para parar]: '))
while num != 999:  
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite mais outro número: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))