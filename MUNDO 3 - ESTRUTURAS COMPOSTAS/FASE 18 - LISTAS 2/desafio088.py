<<<<<<< HEAD
# Programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta. 

from random import randint # sorteio
from time import sleep #processando

lista = []
jogos = []
print('-'*30)
print(' '*4, 'JOGO DA MEGA SENA', ' '*4)
print('-'*30)
quant = int(input('Informe quantos jogos você quer que eu sorteie? '))
total_jogos = 1
while total_jogos <= quant:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) # copia da lista
    lista.clear()
    total_jogos += 1
print('-'*30)
print(' '*3, f'SORTEANDO {quant} JOGOS', ' '*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-'*30)
=======
# Programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta. 

from random import randint # sorteio
from time import sleep #processando

lista = []
jogos = []
print('-'*30)
print(' '*4, 'JOGO DA MEGA SENA', ' '*4)
print('-'*30)
quant = int(input('Informe quantos jogos você quer que eu sorteie? '))
total_jogos = 1
while total_jogos <= quant:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) # copia da lista
    lista.clear()
    total_jogos += 1
print('-'*30)
print(' '*3, f'SORTEANDO {quant} JOGOS', ' '*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-'*30)
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print(' '*8, f'BOA SORTE!', ' '*8)