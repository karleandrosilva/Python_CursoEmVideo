<<<<<<< HEAD
# programa que lê nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostar:  1) Quantas pessoas foram cadastradas.             2) Uma lista com as pessoas mais pesadas.         3) Uma lista com as pessoas mais leves.

galera = []
dados = []
max = min = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('peso: ')))

    if len(galera) == 0:
        max = min = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]

    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    # if resp == 'S':
    #     continue
    # elif resp != 's':
    #     break
    if resp in 'Nn':
        break

print('-'*30)
print(f'Ao todo, foram cadastrado {len(galera)} pessoas')
print(f'O maior peso foi de {max}Kg. Peso de ',end='')
for pessoa in galera:
     if pessoa[1] == max:
         print(f'{pessoa[0]}', end='')
print()
print(f'O menor peso foi de {min}Kg. Peso de',end='')
for pessoa in galera:
     if pessoa[1] == min:
         print(f'{pessoa[0]}', end='')
=======
# programa que lê nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostar:  1) Quantas pessoas foram cadastradas.             2) Uma lista com as pessoas mais pesadas.         3) Uma lista com as pessoas mais leves.

galera = []
dados = []
max = min = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('peso: ')))

    if len(galera) == 0:
        max = min = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]

    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    # if resp == 'S':
    #     continue
    # elif resp != 's':
    #     break
    if resp in 'Nn':
        break

print('-'*30)
print(f'Ao todo, foram cadastrado {len(galera)} pessoas')
print(f'O maior peso foi de {max}Kg. Peso de ',end='')
for pessoa in galera:
     if pessoa[1] == max:
         print(f'{pessoa[0]}', end='')
print()
print(f'O menor peso foi de {min}Kg. Peso de',end='')
for pessoa in galera:
     if pessoa[1] == min:
         print(f'{pessoa[0]}', end='')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print()