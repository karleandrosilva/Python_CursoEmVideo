# criar um programa que leia o ano de nascimento  de 7 pessoas. E no final mostre quais pessoas ainda não são de maior.

from datetime import date 
#atual = date.today().year
contador_maior = 0
contador_menor = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ( 2023 - nasc ) #atual
    if idade >= 21:
        contador_maior = contador_maior + 1
    else:
        contador_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(contador_maior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(contador_menor))
