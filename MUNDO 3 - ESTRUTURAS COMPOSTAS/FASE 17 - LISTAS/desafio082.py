<<<<<<< HEAD
# programa que lê vários números e coloca em uma lista. Depois disso, crie duas listas extras que vão conter apenas os números pares e os números ímpares digitados respectivamente. Ao fina, mostre o conteúdo das três listas geradas.

lista = [0,1,2,3,4,5,6,7,8,9]
lista_par = []
lista_impar = []
print(f'A lista completa é {lista}')
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')

# lista = []
# lista_par = []
# lista_impar = []

# while True:
#     n = int(input(f'Informe um valor: '))
#     lista.append(n)
#     prosseguir = str(input('Deseja Continuar? [S/N]  '))
#     if prosseguir in 'Nn':
#         break
# print(f'A lista completa é {lista}')
# for i in lista:
#     if i % 2 == 0:
#         lista_par.append(i)
#     else:
#         lista_impar.append(i)
# print(f'A lista de pares é {lista_par}')
=======
# programa que lê vários números e coloca em uma lista. Depois disso, crie duas listas extras que vão conter apenas os números pares e os números ímpares digitados respectivamente. Ao fina, mostre o conteúdo das três listas geradas.

lista = [0,1,2,3,4,5,6,7,8,9]
lista_par = []
lista_impar = []
print(f'A lista completa é {lista}')
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')

# lista = []
# lista_par = []
# lista_impar = []

# while True:
#     n = int(input(f'Informe um valor: '))
#     lista.append(n)
#     prosseguir = str(input('Deseja Continuar? [S/N]  '))
#     if prosseguir == 'S':
#         continue
#     elif prosseguir != 's':
#         break
# print(f'A lista completa é {lista}')
# for i in lista:
#     if i % 2 == 0:
#         lista_par.append(i)
#     else:
#         lista_impar.append(i)
# print(f'A lista de pares é {lista_par}')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
# print(f'A lista de ímpares é {lista_impar}')