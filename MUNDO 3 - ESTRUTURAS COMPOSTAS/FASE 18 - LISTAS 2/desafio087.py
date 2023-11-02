<<<<<<< HEAD
# aprimoraro desafio086 e mostrando no final,    1) A soma de todos os valores pares digitados.    2) A soma dos valores da terceira coluna.       3) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = maior = soma_coluna = 0
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-'*30)
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-'*30)
print(f'A soma dos valores pares é: {soma_par}.')
for linha in range(0,3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}.')
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
=======
# aprimoraro desafio086 e mostrando no final,    1) A soma de todos os valores pares digitados.    2) A soma dos valores da terceira coluna.       3) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = maior = soma_coluna = 0
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-'*30)
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-'*30)
print(f'A soma dos valores pares é: {soma_par}.')
for linha in range(0,3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}.')
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
print(f'O maior valor da segunda linha é {maior}.')