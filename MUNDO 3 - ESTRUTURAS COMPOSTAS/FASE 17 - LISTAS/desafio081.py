<<<<<<< HEAD
# programa que lê vários números e coloca em uma lista. Depois disso, mostrar: 1) Quantos números foram digitados. 2) A lista de valores ordenada de forma decresecente. 3) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input(f'Informe um valor: ')))
    prosseguir = str(input('Quer continuar? [S/N]  '.upper()))
    if prosseguir == 'S':
        continue
    elif prosseguir != 's':
        break
print('-='*30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')



=======
# programa que lê vários números e coloca em uma lista. Depois disso, mostrar: 1) Quantos números foram digitados. 2) A lista de valores ordenada de forma decresecente. 3) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input(f'Informe um valor: ')))
    prosseguir = str(input('Quer continuar? [S/N]  '.upper()))
    if prosseguir == 'S':
        continue
    elif prosseguir != 's':
        break
print('-='*30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')



>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
