# Fazer um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual é o seu salário R$'))

novsal = sal + (sal*15/100)

print('O seu salário atual de R${:.2f}, vai ter um aumento de 15%. Agora será dé: R${:.2F}'.format(sal, novsal))