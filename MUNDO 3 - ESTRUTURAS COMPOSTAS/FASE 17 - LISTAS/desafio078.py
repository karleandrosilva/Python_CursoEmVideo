<<<<<<< HEAD
# programa que lê 5 valores númericos digitado pelo úsuario e guarde em uma LISTA. No final ele mostra qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numeros = []
maior = 0
menor = 0
for c in range(0,5):
    lista_numeros.append(int(input(f'Informe um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista_numeros[c]
    else:
        if lista_numeros[c] > maior:
            maior = lista_numeros[c]
        if lista_numeros[c] < menor:
            menor = lista_numeros[c]
print(f'Você digitou os valores {lista_numeros}')
print(f'O MAIOR valor digitado foi {maior} na posição ', end='')
for indice, valor in enumerate(lista_numeros):
    if valor == maior:
        print(f'{indice}...', end='')
print() #quebrar linha
print(f'O MENOR valor digitado foi {menor} na posição ', end='')
for indice, valor in enumerate(lista_numeros):
    if valor == menor:
        print(f'{indice}...', end='')
=======
# programa que lê 5 valores númericos digitado pelo úsuario e guarde em uma LISTA. No final ele mostra qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numeros = []
maior = 0
menor = 0
for c in range(0,5):
    lista_numeros.append(int(input(f'Informe um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista_numeros[c]
    else:
        if lista_numeros[c] > maior:
            maior = lista_numeros[c]
        if lista_numeros[c] < menor:
            menor = lista_numeros[c]
print(f'Você digitou os valores {lista_numeros}')
print(f'O MAIOR valor digitado foi {maior} na posição ', end='')
for indice, valor in enumerate(lista_numeros):
    if valor == maior:
        print(f'{indice}...', end='')
print() #quebrar linha
print(f'O MENOR valor digitado foi {menor} na posição ', end='')
for indice, valor in enumerate(lista_numeros):
    if valor == menor:
        print(f'{indice}...', end='')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print()