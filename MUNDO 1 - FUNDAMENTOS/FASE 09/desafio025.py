# crie um programa que leia um nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite um nome de uma pessoa: ')).strip().lower()


print('Seu nome tem Silva? {}'.format('silva' in nome))