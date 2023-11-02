<<<<<<< HEAD
# programa que cria uma matrix de dimensão 3x3 e preeche com valores lidos pelo teclado. E no final mostrar a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-'*30)
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')
=======
# programa que cria uma matrix de dimensão 3x3 e preeche com valores lidos pelo teclado. E no final mostrar a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))
print('-'*30)
for linha in range(0,3): # linha 
    for coluna in range(0,3): # coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')
>>>>>>> 3eff50a18a354c9d60b98d6b0466bd0988a7266c
    print()