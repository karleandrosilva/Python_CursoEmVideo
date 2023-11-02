# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint #da tabela random importar a tabela randint.
from time import sleep

pc = randint(0,5) #faz o pc sortear um num.

num = int(input('Vou pensar em um número entre 0 e 5. \nTente descobrir: '))
print('PROCESSANDO...')
sleep(3)

if num == pc:
    print('PARABÉNS! Você venceu!')
elif num > 5:
    print('Número só até 5.')
else:
    print('Você perdeu, Eu pensei no número {} e não no {}!'.format(pc, num))

